import os
import sys
import shutil
import argparse

PRESET_FOLDER_DOWNLOADS = {"downloads", "Hämtade filer"}

def get_preset_folder_path(alias):
    return PRESET_FOLDER_DOWNLOADS.get(alias.lower())

def remove_dir(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Directory '{folder_path}' removed successfully")

    except Exception as e:
        print(f"Error removing directory '{folder_path}': {e}")

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully")

    except Exception as e:
        print(f"File '{file_path}' could not be deleted: {e}")
        
def remove_files_by_extension(folder_path, file_extension):
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(file_extension):
                file_path = os.path.join(folder_path, filename)
                os.remove(file_path)
                print(f"File '{file_path}' removed successfully")
    except Exception as e:
        print(f"Error removing files with extension '{file_extension}': {e}")

def delete_temp_files(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if filename.startswith("tmp") or filename.endswith(".temp"):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def clear_downloads():
    downloads_path = os.path.expanduser("~/Downloads")
    delete_temp_files(downloads_path)

def main():
    parser = argparse.ArgumentParser(description="Clear folders based on flags")
    parser.add_argument("path", help="Path to file/folder or use preset")
    parser.add_argument("-f", "--file", action="store_true", help="remove single file")
    parser.add_argument("-d", "--directory", action="store_true", help="remove directory")
    parser.add_argument("-D", "--downloads", action="store_true", help="clear the downloads folder")
    parser.add_argument("-e", "--extension", help="remove files with specific extension")

    args = parser.parse_args()

    if args.file:
        if args.extension:
            print("Error: cannot use extension")
        else:
            remove_file(args.path)
    if args.downloads:
        clear_downloads()
        return
    if args.file:
        remove_file(args.path)
    elif args.directory:
        remove_dir(args.path)
    else:
        print("Please provide a valid flag: -f for file, -d for directory, -D for Downloads.")

if __name__ == "__main__":
    main()