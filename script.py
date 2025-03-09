import os
import subprocess
import shutil
import argparse

def search_and_move_docs(directory, keyword, output_folder_name=None):
    matching_files = []
    
    if not output_folder_name:
        output_folder_name = f"filtered_docs_{keyword.replace(' ', '_')}"
    
    output_folder = os.path.join(directory, output_folder_name)
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.endswith(".doc"):
            file_path = os.path.join(directory, filename)
            
            try:
                result = subprocess.run(['antiword', file_path], capture_output=True)
                text = result.stdout.decode('windows-1252', errors='ignore')
                
                if keyword.lower() in text.lower():
                    matching_files.append(filename)
                    shutil.move(file_path, os.path.join(output_folder, filename))
            
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return matching_files, output_folder 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Search for .doc files containing a keyword and move them to a new folder.",
        usage="python script.py --directory DIRECTORY --keyword KEYWORD [--output OUTPUT]"
    )


    parser.add_argument("--directory", type=str, required=True, help="Path to the folder containing .doc files.")
    parser.add_argument("--keyword", type=str, required=True, help="Keyword to search for in the .doc files.")
    parser.add_argument("--output", type=str, required=False, help="Optional: Custom name for the output folder.")

    args = parser.parse_args()

    matching_files, output_folder = search_and_move_docs(args.directory, args.keyword, args.output)

    if matching_files:
        print(f"\n📂 Moved {len(matching_files)} files containing '{args.keyword}' to '{output_folder}':")
        for file in matching_files:
            print(f"- {file}")
    else:
        print("\nNo matching files found.")
