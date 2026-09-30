from pathlib import Path
import shutil
import logging

log_file = Path.home() / "Documents" / "Sortinghat.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

# Get the path to the user's Downloads folder
downloads = Path.home() / "Downloads"


# Define which file extensions belong to each category
categories = {

    "Pictures": [".jpeg", ".gif", ".jpg", ".png", ".webp"],
    "Videos": [".mp4"],
    "Music": [".mp3", ".wav", ".flac", ".m4a"],
    "Documents": [".pdf", ".docx", ".doc", ".txt"],
    "Installers": [".apk", ".msi", ".exe"],
    "Archives": [".zip", ".7z"],
    "Logs": [".log"]
}

destinations = {
    "Documents": Path.home() / "Documents",
    "Music": Path.home() / "Music",
    "Pictures": Path.home() / "Pictures",
    "Videos": Path.home() / "Videos",
    "Logs": downloads / "Logs",
    "Installers": downloads / "Installers",
    "Archives": downloads / "Archives",
    "Other": downloads / "Other",
}

def categorize_file(item):
    for category, extensions in categories.items():
        if item.suffix.lower() in extensions:
            return category

    return "Other"

def scan_downloads():
    # Store files and their categories
    files_to_move = []

    category_counts = {}


    # Go through each item inside the Downloads folder
    for item in downloads.iterdir():

        # Only work with files, not folders
        if item.is_file():

            category_found = categorize_file(item)

            category_counts[category_found] = category_counts.get(category_found, 0) + 1

            # Store the file and its category
            files_to_move.append((item, category_found))


    return files_to_move, category_counts



def move_files(files_to_save, total_files):

    while True:
        
        # Ask the user if they want to organize their Downloads folder
        prompt = input(f"\nMove these {total_files} files? (y/n): ").strip().lower()

        if prompt not in ("y", "n"):
            print("Please enter y or n.")
            continue

        # Only start if the user enters "y"
        if prompt == "y":

            # Go through every file we found
            for item, category in files_to_save:

                # Get the windows folder for this category
                destination = destinations[category]

                if not destination.exists():
                    destination.mkdir()

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
                try: 
                    # Move the file into the folder
                    shutil.move(item, new_path)

                    logging.info(f"{item.name} → {category}")

                    # Tell the user what happened
                    print(f"{item.name} → {new_path.name}")

                except Exception as error:
                    logging.error(f"{item.name} → FAILED: {error}")
                    print(f"Could not move {item.name}: {error}")

            print("\nDone!")
            break

        else:
            print("Cancelled.")
            break

def main():
    files_to_move, category_counts = scan_downloads()
    total_files = len(files_to_move)

    if total_files == 0:
        print("No files to organise.")
        return

    print(f"\nFound {total_files} files in {downloads}")
    print("Summary:")
    print("="*23)

    for category, count in category_counts.items():
        print(f"{category}: {count}")
    print("="*23)    
    move_files(files_to_move, total_files)
    
main()