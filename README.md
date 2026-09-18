# SortingHat

A simple Python script that automatically organizes files downloaded to your Windows Downloads folder.

## What it does

SortingHat checks the file extension of each file in your Downloads folder and moves it to the appropriate Windows folder.

For example:

```text
Downloads/
├── photo.jpg
├── song.mp3
├── report.pdf
└── video.mp4
```

becomes:

```text
Pictures/
└── photo.jpg

Music/
└── song.mp3

Documents/
└── report.pdf

Videos/
└── video.mp4
```

## Supported file types

| Folder    | Extensions                               |
| --------- | ---------------------------------------- |
| Pictures  | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp` |
| Videos    | `.mp4`                                   |
| Music     | `.mp3`, `.wav`, `.flac`, `.m4a`          |
| Documents | `.pdf`, `.docx`, `.doc`, `.txt`          |

## Features

* Automatically detects file types
* Moves files into Windows' existing folders
* Handles duplicate filenames
* Asks for confirmation before moving anything
* Skips folders
* Uses `pathlib` for file paths
* Uses `shutil` for moving files

## Requirements

* Windows
* Python 3.x

No external Python packages are required.

## Running

Run the script from PowerShell:

```powershell
python sortinghat.py
```

SortingHat will first show what it plans to move:

```text
photo.jpg → Pictures
song.mp3 → Music
report.pdf → Documents

Move these files? (y/n):
```

Enter `y` to move the files or anything else to cancel.

## Duplicate files

If a file with the same name already exists in the destination folder, SortingHat creates a numbered copy instead of overwriting it.

Example:

```text
photo.jpg
photo_1.jpg
photo_2.jpg
```

## Current limitations

Files with unsupported extensions are currently classified as `Other`, but there is no `Other` destination configured yet.

More file types and destinations can be added to the `categories` and `destinations` dictionaries.

## Project

SortingHat is a personal Python project built to practice file handling, dictionaries, loops, `pathlib`, and `shutil`.
