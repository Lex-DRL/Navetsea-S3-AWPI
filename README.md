# **Navetsea**'s Sims 3 ArtWork Preservation Initiative

This repo is an attempt to preserve artwork by [Navetsea](https://navetsea.blogspot.com/) that was published as Sims 3 mods.

> __IMPORTANT__: This project uses Git [Large Files Support (LFS)](https://git-lfs.github.com/).
> 
> Downloading a zip file using the corresponding link under green button on Github **WILL NOT WORK**. You must clone the project with a version of git that has LFS.

Downloading git-LFS repo with GitKraken: [YouTube](https://www.youtube.com/watch?v=S03EEusFxoI) _(I don't use GitKraken, not sure: you might need to install Git itself and Git LFS manually.)_

<details>
<summary>Downloading with SmartGit (git-LFS is included)</summary>

0. [Download SmartGit](https://www.syntevo.com/smartgit/download/) and install it / unpack portable version.
1. _**Repository > Clone**_. Specify the URL of this repo, available here (on GitHub) at the green `Code` button above. If you're not sure which one to use, select HTTPS.
2. Select `initial_pre-LFS` branch and specify local folder to save to. Finish the cloning process.
3. _**Local > LFS > Install...**_
4. Switch to the `main` branch (double-click it, under "origin", in _**Branches**_ window).
5. Wait till it downloads the latest version of files.
</details>

## MTSv
[ModTheSims](https://modthesims.info/d/479460) portal forbids publishing explicit content. So for it, `MTS` variants of the mods were made. They contain censored female textures (crotch area is in barbie-style). Male textures are still full, since "that part" of texture can't be shown, unless a [corresponding additional mod by Cmar](http://sexysims.info/download.php?t=173718) is installed, too.

Full variants of mods are marked as `Adult` in their file name, censored are amrked as `MTSv`.

## Presence table
<details>
<summary>Table</summary>

- ✅ : present
- ❌ : lost
- `-` : never was released

| Mod                       | Full default | Full non-default | MTSv default | MTSv non-default |
| ------------------------- | ------------ | ---------------- | ------------ | ---------------- |
| Normal (revised)          | ✅            | ✅                | ✅            | ✅                |
| Glam                      | ✅            | ✅                | ✅            | ✅                |
| Wild v1 (Hairy v1)        | ✅            | ❌                | -            | -                |
| B.A.S                     | -            | ✅                | -            | -                |
| T.S.I (Asian)             | -            | ✅                | -            | -                |
| **Wild v2 (Hairy v2)**    | -            | ❌                | -            | ✅                |
| G.O.S (Garden of Shadows) | ✅            | ✅                | -            | -                |
| Real1                     | ❌            | ✅                | -            | -                |
| Real2                     | ✅            | ✅                | -            | -                |
| **Cute**                  | ❌            | ❌                | ✅            | ✅                |
| Tan                       | ❌            | ✅                | -            | -                |
| **Glam (revised)**        | ❌            | ❌                | -            | -                |
| T.S.I revised (Asian)     | ✅            | ❌                | -            | ✅                |
| Busty                     | ✅            | ✅                | -            | -                |
| Sexy                      | ✅            | ✅                | -            | ✅                |
| Hot                       | ✅            | ✅                | -            | -                |
| Bad                       | ✅            | ✅                | -            | -                |
| Hairy v3                  | ✅            | ✅                | -            | -                |
| Sweet                     | ✅            | ✅                | -            | -                |
| Model                     | ✅ + futa     | ✅                | ✅            | ✅                |
| Asian                     | ✅            | ✅                | -            | -                |
| Wolf                      | -            | ✅                | -            | -                |
| Hairy v4                  | -            | ✅                | -            | -                |
| BONUS Cstyle              | ✅            | ✅                | -            | -                |

</details>

## Duplicates
<details>
<summary>How duplicate variants of the same mods were treated</summary>

If you try to search for Navetsea's mods yourself, you'll soon discover that there are multiple different binary `.package` files for each mod in the internet. It's unclear what's the difference between them and which one you should choose.

Therefore, I have downloaded all the possible variations of Navetsea's mods that I was able to find and I manually compared them. First, with bit-to-bit comparison. Then, using s3pe v14-0222-1852 I've actually extracted their contents (the textures themselves) and compared those.
When a bunch of duplicates were found, I've chosen the file with the smallest size. As far as I managed to learn it myself, `.package` file is basically just an archive. So if two files have exactly the same contents, they are effectively the same mod. The smaller one is just compressed better.

Feel free to correct me if I got it wrong (other, bigger versions of each file are kept in git history anyway).

Everything from all the following links is already in this repo - in one way or another:

- All the mods available for download on modthesims.info
- The main archive by [wapitawg](https://www.loverslab.com/profile/577239-wapitawg/):
	https://www.loverslab.com/topic/177185-navetsea-face-in-skins-collection-25-skins-in-default-and-non-default-versions/
	
	https://mega.nz/folder/UgBCwbpQ#le0T3O2UCryBMo8qziB3Dg
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

## Reasoning
There's a great 3D/Texture artist [Navetsea](https://navetsea.blogspot.com/) who has published a ton of custom character skintones in a form of mods for Sims 3. Unfortunately, they've published all their work so long ago that internet itself wasn't as developed back then. All the "official" download links in their blog are already dead by now, and what's published on other resources like [modthesims.info](https://modthesims.info/d/479460/face-in-revised-default-amp-non-default-natural-realistic-style-skin.html) is just a tiny fraction of what was created. Forum threads contain download links scattered over multiple forums, most of which are already dead, too. And those links that still work... Well, none of them contain _**ALL**_ the artwork in a single place.

So, before it's too late, this repo was created, to keep the amazing work.

## Disclaimer
In no way, shape or form the author of this repo takes credit for the artworks. As explicitly, stated, these mods were authored by [Navetsea](https://navetsea.blogspot.com/). And they were archived/recovered/shared by various users on community forums. [Credits](/CREDITS.md)
