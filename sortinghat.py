from pathlib import Path
import shutil

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
}

destinations = {
    "Documents": Path.home() / "Documents",
    "Music": Path.home() / "Music",
    "Pictures": Path.home() / "Pictures",
    "Videos": Path.home() / "Videos",
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

    # Go through each item inside the Downloads folder
    for item in downloads.iterdir():

        # Only work with files, not folders
        if item.is_file():

            category_found = categorize_file(item)

            # Store the file and its category
            files_to_move.append((item, category_found))

            # Show what the program found
            print(f"{item.name} → {category_found}")

    return files_to_move



def move_files(files_to_save):


    # Ask the user if they want to organize their Downloads folder
    prompt = input("\nMove these files? (y/n): ").lower()

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

            # Move the file into the folder
            shutil.move(item, new_path)

            # Tell the user what happened
            print(f"{item.name} → {new_path.name}")

        print("\nDone!")

def main():
    files_to_move = scan_downloads()
    move_files(files_to_move)

main()