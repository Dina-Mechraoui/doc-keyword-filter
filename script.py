import os
import subprocess
import shutil 

def search_and_move_docs(directory, keyword):
    matching_files = []
    
    output_folder = os.path.join(directory, "new_folder_name")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.endswith(".doc"):
            file_path = os.path.join(directory, filename)
            
            try:
                # Extract text using antiword and force Windows-1252 encoding
                result = subprocess.run(['antiword', file_path], capture_output=True)
                
                # Decode using Windows-1252 to fix utf-8 errors
                text = result.stdout.decode('windows-1252', errors='ignore')
                
                if keyword.lower() in text.lower():
                    matching_files.append(filename)
                    shutil.move(file_path, os.path.join(output_folder, filename))
            
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return matching_files, output_folder

directory_path = "path_to_folder_you_want_to_filter"
keyword_to_search = "filtering_keyword" 

matching_files, output_folder = search_and_move_docs(directory_path, keyword_to_search)

if matching_files:
    print(f"\n📂 Moved {len(matching_files)} files containing '{keyword_to_search}' to '{output_folder}':")
    for file in matching_files:
        print(f"- {file}")
else:
    print("\nNo matching files found.")
