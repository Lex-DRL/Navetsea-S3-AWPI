# **Navetsea**'s `Sims 3` ArtWork Preservation Initiative

This repo is an attempt to preserve artwork by [Navetsea](https://navetsea.blogspot.com/) that was published as Sims 3 mods.

<p align="center">
	<img src="/preview-images/_facial_skin_comparison.gif" alt="Facial skin comparison"/>
</p>

<details>
<summary>Table of contents</summary>

- [Reasoning / About](#reasoning--about)
- [Naming explained](#naming-explained)
	* [General scheme](#general-scheme)
	* [Folder number](#folder-number)
	* [MTSv vs Adult](#mtsv-vs-adult)
	* [Default vs non-default](#default-vs-non-default)
- [Present mods](#present-mods)
	* [Ancient mods](#ancient-mods)
	* [Relevant (newer, up-to-date) mods](#relevant-newer-up-to-date-mods)
- [Technical details](#technical-details)
	* [Duplicates](#duplicates)
	* [Sources](#sources)
	* [File timestamps](#file-timestamps)
	* [Modding tools](#modding-tools)
- [Contributing](#contributing)
- [Disclaimer / Credits](#disclaimer--credits)
</details>

## Reasoning / About
There's a great 3D/Texture artist [Navetsea](https://navetsea.blogspot.com/) who has published a ton of custom character skintones in a form of mods for Sims 3. Unfortunately, they've published all their work so long ago that internet itself wasn't as developed back then. All the "official" download links in their blog are already dead by now, and what's published on other resources like [modthesims.info](https://modthesims.info/downloads/ts3/342/?showType=1&t=normal&p=1&csort=0&u=57347) is just a tiny fraction of what was created.

Forum threads contain download links scattered over multiple forums, most of which are already dead, too. And those links that still work... Well, none of them contain _**ALL**_ the artwork in a single place.

So, before it's too late, this repo was created, to save the amazing work.

## Naming explained
### General scheme
All Navetsea's skintone mods are called `F-IN TS3...`. This is the naming brought from earlier work in `Sims 2` skins:

- `F-IN` = "face texture included";
- `TS3` = `The Sims 3`.

In earlier (ancient) mods, Navetsea intended to name them like `F-IN01`, `F-IN02` etc. It's supposed to indicate newer versions. But soon it became clear that multiple version branches can co-exist (they're called editions now).

Therefore, Navetsea switched to a more flexible scheme:

`F-IN TS3 {MTSv/Adult} {Edition name} [optional version] {default/nondefault}`.

E.g:

- `F-IN TS3 MTSv glam default`
- `F-IN TS3 Adult Hairy v3 nondefault`

### Folder number
Each mod edition is in it's own subfolder, starting with a number. It represents the order of apperance of the skin on [Navetsea blog](https://navetsea.blogspot.com/).

### MTSv vs Adult
[ModTheSims](https://modthesims.info/d/479460) portal forbids publishing explicit content. So for it, `MTS` variants of the mods were made. They contain censored female textures (crotch area is in barbie-style). Male textures are still full, since "that part" of texture can't be shown, unless a [corresponding additional mod by Cmar](http://sexysims.info/download.php?t=173718) is installed, too.

Full variants of mods are marked as `Adult` in their file name, censored are marked as `MTSv`.

### Default vs non-default
`Default` mods replace the built-in (default) appearance. **THERE COULD BE ONLY ONE DEFAULT REPLACEMENT** installed at a time (not only from Navetsea's mods, but across your whole `Sims 3` profile).

`Non-default` ones add a new skintone to the pallete.

## Present mods
> __IMPORTANT__: If you have any of the missing mods, **PLEASE SHARE THEM** *(See [Contributing](#contributing))*.

### Ancient mods
From old (outdated) mods, all of them are present. These mods are inside `00 ancient skins do not install` folder. You shouldn't need them anyway, but here's the list of those just in case. All of them contain only default replacements:

- [**SS2 v1 female + v2 unisex**](/mods/00%20ancient%20skins%20do%20not%20install/SS2%20v1%20female%20%2B%20v2%20unisex)
- [**V2B**](/mods/00%20ancient%20skins%20do%20not%20install/V2B)
- [**V2C**](/mods/00%20ancient%20skins%20do%20not%20install/V2C)

### Relevant (newer, up-to-date) mods

- ✅ : present
- ❌ : lost
- `—` : never was released

| Mod                                                                       | Full default | Full non-default | MTSv default | MTSv non-default |
| ------------------------------------------------------------------------- | ------------ | ---------------- | ------------ | ---------------- |
| [Normal revised](/mods/01%20Normal%20revised)                             | ✅            | ✅                | ✅            | ✅                |
| [Glam](/mods/02%20Glam)                                                   | ✅            | ✅                | ✅            | ✅                |
| [Wild (Hairy) v1](/mods/03%20Wild%20(Hairy)%20v1)                         | ✅            | ❌                | —            | —                |
| [B.A.S (Freckled)](/mods/04%20B.A.S%20(Freckled))                         | —            | ✅                | —            | —                |
| [T.S.I (Asian)](/mods/05%20T.S.I%20(Asian))                               | —            | ✅                | —            | —                |
| [**❌ Wild (Hairy) v2**](/mods/06%20Wild%20(Hairy)%20v2)                   | —            | ❌                | —            | ✅                |
| [G.o.S (Garden of Shadows)](/mods/07%20G.o.S%20(Garden%20of%20Shadows))   | ✅            | ✅                | —            | —                |
| [**❌ V2R**](/mods/08%20V2R) (updated `V2C` / elements of `Real 1`)        | ❌            | ❌                | —            | —                |
| [Real 1](/mods/09%20Real%201)                                             | ❌            | ✅                | —            | —                |
| [Real 2](/mods/10%20Real%202)                                             | ✅            | ✅                | —            | —                |
| [**❌ Cute**](/mods/11%20Cute)                                             | ❌            | ❌                | ✅            | ✅                |
| [Tan](/mods/12%20Tan)                                                     | ❌            | ✅                | —            | —                |
| [**❌ Glam revised**](/mods/13%20Glam%20revised)                           | ❌            | ❌                | —            | —                |
| [T.S.I (Asian) v2 (revised)](/mods/14%20T.S.I%20(Asian)%20v2%20(revised)) | ✅            | ❌                | —            | ✅                |
| [Busty](/mods/15%20Busty)                                                 | ✅            | ✅                | —            | —                |
| [Sexy](/mods/16%20Sexy)                                                   | ✅            | ✅                | —            | ✅                |
| [Hot](/mods/17%20Hot)                                                     | ✅            | ✅                | —            | —                |
| [Bad](/mods/18.1%20Bad)                                                   | ✅            | ✅                | —            | —                |
| [Hairy v3](/mods/18.2%20Hairy%20v3)                                       | ✅            | ✅                | —            | —                |
| [Sweet](/mods/19%20Sweet)                                                 | ✅            | ✅                | —            | —                |
| [Model](/mods/20%20Model)                                                 | ✅ + futa     | ✅                | ✅            | ✅                |
| [Asian](/mods/21%20Asian)                                                 | ✅            | ✅                | —            | —                |
| [Wolf](/mods/22%20Wolf)                                                   | —            | ✅                | —            | —                |
| [Hairy v4](/mods/23%20Hairy%20v4)                                         | —            | ✅                | —            | —                |
| [BONUS Cstyle](/mods/BONUS%20Cstyle)                                      | ✅            | ✅                | —            | —                |

## Technical details
### Duplicates
<details>
<summary>How duplicate variants of the same mods were treated</summary>

If you try to search for Navetsea's mods yourself, you'll soon discover that there are multiple different binary `.package` files for each mod in the internet. It's unclear what's the difference between them and which one you should choose.

Therefore, I have downloaded all the possible variations of Navetsea's mods that I was able to find and I manually compared them. First, with bit-to-bit comparison. Then, using s3pe v14-0222-1852 I've actually extracted their contents (the textures themselves) and compared those.
When a bunch of duplicates were found, I've chosen the file with the smallest size. As far as I managed to learn it myself, `.package` file is basically just an archive. So if two files have exactly the same contents, they are effectively the same mod. The smaller one is just compressed better.

Feel free to correct me if I got it wrong (other, bigger versions of each file are kept in git history anyway).
</details>

### Sources
<details>
<summary>Everything from all the following links is already in this repo - in one way or another</summary>

- All the mods available for download on:
	
	- [modthesims.info](https://modthesims.info/downloads/ts3/342/?showType=1&t=normal&p=1&csort=0&u=57347)
	- [sexysims.info](http://sexysims.info/download.php?t=173792)
- The main archive by [wapitawg](https://www.loverslab.com/profile/577239-wapitawg/):
	
	- https://www.loverslab.com/topic/177185-navetsea-face-in-skins-collection-25-skins-in-default-and-non-default-versions/
	- https://mega.nz/folder/UgBCwbpQ#le0T3O2UCryBMo8qziB3Dg
	- They specified there that, in turn, their own sources were:
		* [Insimadult board](http://www.insimadult.org/index.php?action=profile;u=73817;sa=showTopics)
		* [CStyle forums](https://cstylessims3forum.forumotion.com/)
		* [Garden of Shadows forums](https://gardenofshadows.org.uk/gardenofshadows/index.php)
- https://www.loverslab.com/topic/77817-navetsea-skins/#comment-1897886 / http://www.mediafire.com/download/cd33i3frcw22uf3/navetsea_skins.rar
- https://www.loverslab.com/topic/77817-navetsea-skins/#comment-1897886 / https://www.mediafire.com/folder/ta2jxwevxenqs/navetsea_skins
- https://www.loverslab.com/topic/77817-navetsea-skins/#comment-1899629 / http://simfileshare.net/download/144124/
- https://www.loverslab.com/topic/77817-navetsea-skins/#comment-2152693
- https://www.loverslab.com/topic/77817-navetsea-skins/#comment-2158835
- https://www.loverslab.com/topic/77817-navetsea-skins/page/2/#comment-3253139

- https://modthesims.info/showthread.php?p=4616774#post4616774 / https://www.mediafire.com/file/4m5p4gspeyhg6k7/navetsea_F-IN_TS3_Adult_real2_default.7z/file
- https://modthesims.info/showthread.php?p=5095588#post5095588 / https://www.mediafire.com/file/7jwx7l5jye4sdmd/navetseaF-INTS3MTSvcutenondefault.7z/file
- https://modthesims.info/showthread.php?p=5175045#post5175045 / http://depositfiles.com/files/vtcqxi5nx
- https://modthesims.info/showthread.php?p=5441275#post5441275 / https://mega.nz/#!3J8wGKZS!qMpsqvqjprPyGhfUlbJyqGG96I7fJzZygeDyFBWrwwI

</details>

### File timestamps
Since git doesn't preserve file attributes, I've created a small python script, `timestamps_sync.py`.
It simply remembers timestamp of each mod into `timestamps.txt`. You can run it from command line with `python timestamps_sync.py` (python 3 must be installed).

The script synchronizes file modification time between the actual mod file and the aforementioned `timestamps.txt` cache. When they differ, the earliest date/time is chosen and applied for both. I.e., if you launch the script right after cloning the repo, all the mods will get their modification time from the cache.

This might become handy in future, if someone would need to know when each mod was released.

### Modding tools
Navetsea themself say that they used:

- [S3PE](http://www.simlogical.com/s3pe.htm) by Peter & Inge Jones
- [Skininator](https://modthesims.info/d/389488/skininator-a-tool-to-make-non-default-and-default-custom-skins-new-version-1-10-2013.html) by [CmarNYC](https://modthesims.info/member.php?u=3216596)

## Contributing
If you can contribute to the archive, feel free to fork the repo and create a pull request with your additions.

**OR**, if you have a missing mod version on hand, but are very unfamiliar with git or GitHub (and don't want to dig into it), you can help, too. Just [create a new issue](../../issues) and attach a file there.

Let's restore the archive together!

## Disclaimer / Credits
In no way, shape or form the author of this repo takes credit for the artworks. As explicitly stated, these mods were authored by [Navetsea](https://navetsea.blogspot.com/). And they were archived/recovered/shared by various users on community forums. [Credits](/CREDITS.md)
