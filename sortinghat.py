from pathlib import Path
import shutil
import logging

log_file = Path.home() / "Documents" / "Sortinghat.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

# Get the path to folder being organised
folders = {
    "Downloads" : Path.home() / "Downloads",
    "Desktop": Path.home() / "Desktop",
    "Documents": Path.home() / "Documents",
    "Videos": Path.home() / "Videos",
    "Pictures": Path.home() / "Pictures",
    "Music": Path.home() / "Music"
}

ignore_extensions = {
    ".lnk",
    ".url",
    ".db",
    ".ini"
}

ignore_files = {
    "SortingHat.log"
}

# Define which file extensions belong to each category
categories = {

    "Pictures": [".jpeg", ".gif", ".jpg", ".png", ".webp"],
    "Videos": [".mp4"],
    "Music": [".mp3", ".wav", ".flac", ".m4a"],
    "Documents": [".pdf", ".docx", ".doc", ".txt"],
    "Installers": [".apk", ".msi", ".exe"],
    "Archives": [".zip", ".7z"],
    "Logs": [".log"],
    "Bitmap": [".bmp"],
    "DiskImages": [".iso"]
}

destinations = {
    "Documents": Path.home() / "Documents",
    "Music": Path.home() / "Music",
    "Pictures": Path.home() / "Pictures",
    "Videos": Path.home() / "Videos",
    "Logs": folders["Downloads"] / "Logs",
    "Installers": folders["Downloads"] / "Installers",
    "Archives": folders["Downloads"] / "Archives",
    "Other": folders["Downloads"] / "Other",
    "DiskImages": folders["Downloads"] / "DiskImages"
}

def categorize_file(item):
    for category, extensions in categories.items():
        if item.suffix.lower() in extensions:
            return category

    return "Other"

def scan_folder(folder):
    already_organized = 0

    # Store files and their categories
    files_to_move = []

    category_counts = {}


    # Go through each item inside the folder
    for item in folder.iterdir():

        # Only work with files, not folders
        if (
            item.is_file()
            and item.suffix.lower() not in ignore_extensions
            and item.name not in ignore_files
            ):

            category_found = categorize_file(item)

            if item.parent == destinations.get(category_found):
                already_organized += 1
                continue

            category_counts[category_found] = category_counts.get(category_found, 0) + 1

            # Store the file and its category
            files_to_move.append((item, category_found))


    return files_to_move, category_counts, already_organized

def get_unique_path(destination, item):
    # Create the path where the file will be moved
    new_path = destination / item.name

    # Check if a file with the same name already exists
    if new_path.exists():

        # Start duplicate counter
        counter = 1

        # Keep trying new names until we find one that doesn't exist
        while True:
            new_name = f"{item.stem}_{counter}{item.suffix}"
            new_path = destination / new_name

            if not new_path.exists():
                break

            counter += 1

    return new_path

def create_destination(destination):
    if not destination.exists():
        destination.mkdir(exist_ok = True)

def move_files(files_to_move, folder, dry_run=False):
    total_files = len(files_to_move)

    while True:
        
        action = "Preview" if dry_run else "Move"
        prompt = input(f"\n{action} these {total_files} files from {folder}? (y/n): ").strip().lower() 

        if prompt not in ("y", "n"):
            print("Please enter y or n.")
            continue

        # Only start if the user enters "y"
        if prompt == "y":
            moved = 0
            failed = 0

            if dry_run:
                for item, category in files_to_move:
                    destination = destinations[category]
                    new_path = get_unique_path(destination, item)
                    print(f"Would move: {item.name} → {new_path}")

                break

            # Go through every file we found
            for item, category in files_to_move:

                # Get the windows folder for this category
                destination = destinations[category]

                create_destination(destination)

                new_path = get_unique_path(destination, item)
                
                try: 
                    # Move the file into the folder
                    shutil.move(item, new_path)
                    moved += 1

                    logging.info(f"{item.name} → {new_path}")

                    # Tell the user what happened
                    print(f"{item.name} → {new_path}")

                except Exception as error:
                    failed += 1
                    logging.error(f"{item.name} → FAILED: {new_path} → {error}")
                    print(f"Could not move {item.name}: {error}")


            print("\nDone!")
            print(f"Moved: {moved}")
            if failed > 0:
                print(f"Failed: {failed}")
            break

        else:
            print("Cancelled.")
            break

def display_summary(category_counts):
    print("Summary:")
    print("="*23)

    for category, count in category_counts.items():
        print(f"{category}: {count}")
    print("="*23)   

def main():
    print("Choose a folder to organize:")
    for number, folder_name in enumerate(folders, start=1):
        print(f"{number}. {folder_name}")

    choice = input("Enter your choice: ")

    if not choice.isdigit() or not 1 <= int(choice) <= len(folders):
        print("Invalid choice.")
        return

    choice = int(choice)

    folder_name = list(folders)[choice - 1]
    folder = folders[folder_name]

    files_to_move, category_counts, already_organized = scan_folder(folder)
    total_files = len(files_to_move)

    if total_files == 0:
        print("No files to organise.")
        print(f"Already organized: {already_organized}")
        return

    print(f"\nFound {total_files} files in {folder}")

    display_summary(category_counts)

    print(f"Already organized: {already_organized}")
    while True:

        dry_run = input("\nDry run? (y/n): ").strip().lower()

        if dry_run == "y": 
            move_files(files_to_move, folder, dry_run=True)
        elif dry_run == "n":
            move_files(files_to_move, folder)
        else:
            print("Please enter y or n.")

if __name__ == "__main__":
    main()