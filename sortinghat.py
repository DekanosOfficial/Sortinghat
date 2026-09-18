from pathlib import Path
import shutil

# Get the path to the user's Downloads folder
downloads = Path.home() / "Downloads"

# Define which file extensions belong to each category
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

# Store files and their categories
files_to_move = []

# Go through each item inside the Downloads folder
for item in downloads.iterdir():

    # Only work with files, not folders
    if item.is_file():

        # Assume the file doesn't have a category
        category_found = None

        # Go through each category and its list of extensions
        for category, extensions in categories.items():

            # Check if the file's extension belongs to this category
            if item.suffix.lower() in extensions:
                category_found = category
                break

        # If no category was found, put the file in Other
        if category_found is None:
            category_found = "Other"

        # Store the file and its category
        files_to_move.append((item, category_found))

        # Show what the program found
        print(f"{item.name} → {category_found}")


# Ask the user if they want to organize their Downloads folder
prompt = input("\nMove these files? (y/n): ").lower()

# Only start if the user enters "y"
if prompt == "y":

    # Go through every file we found
    for item, category in files_to_move:

        # Create the category folder path
        destination = downloads / category

        # Create the folder if it doesn't exist
        destination.mkdir(exist_ok=True)

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