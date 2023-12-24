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
        
def main():
    parser = argparse.ArgumentParser(description="Clear folders based on flags")
    parser.add_argument("path", help="Path to file/folder or use preset")
    parser.add_argument("-f", "--file", action="store_true", help="remove single file")
    parser.add_argument("-d", "--directory", action="store_true", help="remove directory")
    parser.add_argument("-D", "--downloads", action="store_true", help="clear the downloads folder")

    args = parser.parse_args()
    
    if args.downloads:
        folder_path = get_preset_folder_path("downloads")
        if folder_path:
            args.path = folder_path
        else:
            print("Error: Downloads folder path not configured.")
            return
        
    if args.file:
        remove_file(args.path)
    elif args.directory:
        remove_dir(args.path)
    else:                                                                                   
        print(f"Please provide valid flag: -r for file, -R for directory, -d for Downloads.")
        
        if __name__ == "__main__":
            main()
        

   
        
