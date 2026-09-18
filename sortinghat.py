from pathlib import Path
import shutil
import logging

# get the path to the user's downloads folder
downloads = Path.home() / "Downloads"

# Define which fiel extension belongs to which category
categories = {
    "Installers": [".exe", ".msi"],
    "Archives": [".zip"],
    "Web": [".html"],
    "Images": [".jpeg", ".gif", ".jpg", ".png", ".webp"],
    "Videos": [".mp4"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a"],
    "Documents": [".pdf", ".docx", ".doc", ".txt"],
    "Torrents": [".torrent"],
}

def categorize_file(file):
    for catergory, extensions in categories.items():
        if file.suffix.lower() in extensions:
            return catergory

    return "Other"

def scan_downloads():
    files_to_move = []

    for item in downloads.iterdir():

        if item.name == "sortinghat.py":
            continue

        if not item.is_file():
            continue

        category = categorize_file(item)

        files_to_move.append((item, category))

    return files_to_move

def show_summary(files_to_move):
    file_counts ={}

    for item, category in files_to_move:
        file_counts[category] = file_counts.get(category, 0) + 1
    print("\nSortingHat")
    print("-------------------")

    for category, count in file_counts.items():
        print(f"{category}: {count}")

    print(f"\nTotal: {len(files_to_move)} files")

def main():

    files_to_move = scan_downloads()

    show_summary(files_to_move)

    prompt = input("\nMove these files? (y/n)\n>> ").lower()

    if prompt == "y":
        # move_files(files_to_move)
        print("test move")
    else:
        print("Nothing was moved.")

if __name__ == "__main__":
    main()