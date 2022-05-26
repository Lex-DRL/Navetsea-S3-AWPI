#!/usr/bin/env python
# encoding: utf-8

"""
This script stores file timestamps in a cache file and re-applies them to the packages themselves.
Useful to keep track of approximate dates each mod was released.
"""

__author__ = 'Lex Darlog (DRL)'

import typing as _t
from typing import (
	Union as _U,
	Optional as _O,
	List, Tuple, Set, Dict, Iterable,
)

import errno
from fnmatch import translate as glob_re
from datetime import datetime as dt, timedelta as td, timezone
from dataclasses import dataclass
from os import stat, utime, walk, PathLike
import re
from pathlib import Path
from sys import platform


ROOT_DIR: Path = Path(__file__).parent
IS_WIN = platform.startswith('win')


# noinspection PyBroadException
try:
	TZ_UTC: timezone = timezone.utc
except Exception:
	TZ_UTC = timezone(td(0))
TZ_LOCAL = dt.now(tz=TZ_UTC).astimezone().tzinfo

_ns_in_sec: int = 1_000_000_000
_t_path = _U[_t.AnyStr, PathLike]


def _dt_from_ns(ns: _U[int, float], tz: timezone = None) -> dt:
	if tz is None:
		tz = TZ_LOCAL
	return dt.fromtimestamp(ns / _ns_in_sec, tz=tz)


def _ns_from_dt(_dt: dt) -> int:
	return int(_dt.timestamp() * _ns_in_sec + 0.5)


def _symlinks_arg_platform_decorator(symlinks_arg_index: int):
	"""
	Makes function to completely ignore `follow_symlinks` argument on Windows.
	Thanks to the decorator, the resulting function is condition-less and yet platform-specific.
	"""
	symlinks_arg_index = max(int(symlinks_arg_index), 0)

	def _wrapper(f: callable):
		if not IS_WIN:
			# for unix - use the function as is
			return f

		# for windows - completely ignore `follow_symlinks` argument
		def _func(*args, follow_symlinks=True, **kwargs):
			return f(*args[:symlinks_arg_index], follow_symlinks=True, **kwargs)
		return _func

	return _wrapper


class FileTimeStamp(int):
	def datetime(self, tz: timezone = None):
		return FileDateTime(
			_dt_from_ns(self, tz=tz)
		)

	@_symlinks_arg_platform_decorator(3)
	def _to_file(self, path: _t_path, atime: int, follow_symlinks=True):
		utime(path, ns=(atime, self), follow_symlinks=follow_symlinks, )


try:
	_dataclass_dec = dataclass(slots=True)
except Exception:
	_dataclass_dec = dataclass()


_dt_threshold = td(milliseconds=500)


@_dataclass_dec
class FileDateTime:
	datetime: dt

	_str_format: str = "%Y-%m-%d.%H:%M:%S.%f.UTC%z"

	def timestamp(self):
		return FileTimeStamp(
			_ns_from_dt(self.datetime)
		)

	def utc(self):
		return self.datetime.astimezone(tz=TZ_UTC)

	def to_str(self):
		return self.utc().strftime(self._str_format)

	@classmethod
	def from_str(cls, string: str, tz: timezone = None):
		if tz is None:
			tz = TZ_LOCAL
		datetime = dt.strptime(string, cls._str_format).astimezone(tz=tz)
		# noinspection PyArgumentList
		return cls(datetime)

	@classmethod
	def from_file(cls, path: _t_path, follow_symlinks=True, tz: timezone = None):
		"""Returns modification time as `FileDateTime` and access time (ns) as int."""
		file_stat = stat(path, follow_symlinks=follow_symlinks)
		return FileTimeStamp(file_stat.st_mtime_ns).datetime(tz=tz), file_stat.st_atime_ns

	def to_file(self, path: _t_path, follow_symlinks=True, max_attempts=3):
		"""Returns an attempt at which the timestamp was successfully set. 0 if it was already the same."""
		# noinspection PyProtectedMember
		to_file_f = self.timestamp()._to_file
		file_dt, file_atime = self.from_file(path, follow_symlinks=follow_symlinks)
		goal_datetime = self.datetime

		if abs(file_dt.datetime - goal_datetime) < _dt_threshold:
			return 0
		for _i in range(max(max_attempts, 1)):
			to_file_f(path, file_atime, follow_symlinks=follow_symlinks)
			file_dt = self.from_file(path, follow_symlinks=follow_symlinks)[0]
			if abs(file_dt.datetime - goal_datetime) < _dt_threshold:
				return _i + 1
		raise OSError(errno.EPERM, f"Can't set timestamp on file: {path}")


_t_matcher_f = _t.Callable[[str], _O[_t.Match]]


def glob_to_re_match(glob: str, flags=re.IGNORECASE) -> _t_matcher_f:
	re_str = glob_re(glob)
	return re.compile(re_str, flags=flags).match


def glob_matchers(*patterns: str) -> Dict[str, _t_matcher_f]:
	return {x: glob_to_re_match(x) for x in patterns}


@_dataclass_dec
class TimeSync:
	root_dir: Path = ROOT_DIR
	cache_file: str = 'timestamps.txt'
	matched = glob_matchers('*.package', )
	excluded = glob_matchers('.*', '__pycache__', )
	sep = '|'

	@property
	def cache_path(self):
		return Path(self.root_dir) / self.cache_file

	def open_cache_file(self, mode='rt'):
		return self.cache_path.open(mode, encoding='utf-8', newline='\n')

	def file_paths(self):
		match_funcs = tuple(self.matched.values())
		exclude_funcs = tuple(self.excluded.values())

		def is_match(file_name: str):
			return any(x(file_name) for x in match_funcs)

		def is_excluded(file_name: str):
			return any(x(file_name) for x in exclude_funcs)

		for root, dirs, files in walk(str(self.root_dir)):
			dirs[:] = (x for x in dirs if not is_excluded(x))
			files[:] = (x for x in files if is_match(x) and not is_excluded(x))
			for file in files:
				yield Path(root) / file

	def file_timestamps(self, follow_symlinks=True):
		root_path = Path(self.root_dir)
		for path in self.file_paths():
			rel_path = path.relative_to(root_path)
			yield rel_path.as_posix(), FileDateTime.from_file(path, follow_symlinks=follow_symlinks)[0]

	def cached_timestamps(self):
		sep = self.sep
		with self.open_cache_file('rt') as cache_file:
			try:
				lines: List[str] = [x.lstrip().rstrip('\r\n') for x in cache_file.readlines()]
			except FileNotFoundError:
				return
		for line in lines:
			split = line.split(sep=sep)
			if len(split) < 2:
				continue
			timestamp_str, *split = split
			rel_path = sep.join(split)
			yield Path(rel_path).as_posix(), FileDateTime.from_str(timestamp_str)

	def _saved_cache_lines(self, out_timestamps: Dict[str, FileDateTime]):
		sep = self.sep
		for rel_path, out_ts in out_timestamps.items():
			yield f'{out_ts.to_str()}{sep}{rel_path}\n'

	def sync_min_time(self, follow_symlinks=True, max_attempts=3):
		root_path = Path(self.root_dir)

		cached_changed = False
		updated_files: Set[str] = set()
		file_timestamps = dict(self.file_timestamps(follow_symlinks=follow_symlinks))
		cached_timestamps = dict(self.cached_timestamps())

		to_forget = {k for k in cached_timestamps.keys() if k not in file_timestamps}
		if to_forget:
			cached_changed = True
			for rem_k in to_forget:
				cached_timestamps.pop(rem_k)

		out_timestamps: Dict[str, FileDateTime] = dict()

		for rel_path, file_ts in file_timestamps.items():
			if rel_path not in cached_timestamps:
				out_timestamps[rel_path] = file_ts
				cached_changed = True
				continue

			cached_ts = cached_timestamps[rel_path]
			cached_dt = cached_ts.datetime
			file_dt = file_ts.datetime
			if abs(file_dt - cached_dt) < _dt_threshold:
				out_timestamps[rel_path] = file_ts
				continue

			# timestamps are not equal: either we need to update file or cache.
			if cached_dt < file_dt:
				# we need to update file timestamp
				updated_files.add(rel_path)
				out_timestamps[rel_path] = cached_ts
			else:
				# we need to update cache
				out_timestamps[rel_path] = file_ts
				cached_changed = True

		if not(updated_files or cached_changed):
			print("Files' timestamps are the same as in cache.")

		# update timestamps on files:
		if updated_files:
			print("Updated timestamps:")
			sep = self.sep
			for rel_path in updated_files:
				out_ts = out_timestamps[rel_path]
				print(f"{out_ts.to_str()}{sep}{rel_path}")
				out_ts.to_file(root_path / rel_path, follow_symlinks=follow_symlinks, max_attempts=max_attempts)

		if cached_changed:
			print("Updating cache...")
			with self.open_cache_file('wt') as cache_file:
				cache_file.writelines(self._saved_cache_lines(out_timestamps))


if __name__ == '__main__':
	TimeSync().sync_min_time()
	input("Done")
