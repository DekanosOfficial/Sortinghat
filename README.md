# SortingHat

A simple Python script that automatically organizes files downloaded to your Windows Downloads folder.

## What it does

SortingHat checks the file extension of each file in your Downloads folder and moves it to the appropriate location.

For example:

```text
Downloads/
├── photo.jpg
├── song.mp3
├── report.pdf
├── setup.exe
└── backup.zip
```

becomes:

```text
Pictures/
└── photo.jpg

Music/
└── song.mp3

Documents/
└── report.pdf

Downloads/Installers/
└── setup.exe

Downloads/Archives/
└── backup.zip
```

## Supported file types

| Category   | Extensions                               | Destination            |
| ---------- | ---------------------------------------- | ---------------------- |
| Pictures   | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp` | Windows Pictures       |
| Videos     | `.mp4`                                   | Windows Videos         |
| Music      | `.mp3`, `.wav`, `.flac`, `.m4a`          | Windows Music          |
| Documents  | `.pdf`, `.docx`, `.doc`, `.txt`          | Windows Documents      |
| Installers | `.apk`, `.msi`, `.exe`                   | `Downloads/Installers` |
| Archives   | `.zip`, `.7z`                            | `Downloads/Archives`   |
| Other      | Unsupported extensions                   | `Downloads/Other`      |

## Features

* Automatically detects file types by extension
* Moves pictures, videos, music, and documents into Windows' existing folders
* Separates installers and archives into dedicated Downloads folders
* Places unsupported file types into `Downloads/Other`
* Creates `Installers`, `Archives`, and `Other` folders when needed
* Handles duplicate filenames without overwriting existing files
* Asks for confirmation before moving anything
* Skips folders
* Uses Python's built-in `pathlib` and `shutil` modules

## Requirements

* Windows
* Python 3.x

No external Python packages are required.

## Running

Run the script from PowerShell:

```powershell
python sortinghat.py
```

SortingHat first shows what it plans to move:

```text
photo.jpg → Pictures
song.mp3 → Music
report.pdf → Documents
setup.exe → Installers
backup.zip → Archives

Move these files? (y/n):
```

Enter `y` to move the files.

Anything other than `y` cancels the operation.

## Duplicate files

SortingHat does not overwrite existing files.

If a file with the same name already exists, it creates a numbered filename:

```text
photo.jpg
photo_1.jpg
photo_2.jpg
```

## Current limitations

* File classification is based only on file extensions.
* Only the extensions listed above are currently supported.
* Files that don't match a category are placed in `Downloads/Other`.
* SortingHat currently operates on the user's Windows Downloads folder.
* It does not organize files inside subfolders.

## Project

SortingHat is a personal Python project built to practice file handling, dictionaries, loops, `pathlib`, `shutil`, and program structure.

The project is being developed incrementally, with modularization and additional features planned for future versions.
