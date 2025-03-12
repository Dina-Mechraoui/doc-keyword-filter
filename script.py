import os
import subprocess
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import sys

def get_antiword_path():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(os.path.dirname(__file__))
    
    antiword_path = os.path.join(base_path, "antiword")
    if os.path.exists(antiword_path):
        return antiword_path
    else:
        return None

ANTIWORD_PATH = get_antiword_path()

if not ANTIWORD_PATH or not os.path.exists(ANTIWORD_PATH):
    messagebox.showerror("Error", "Antiword not found! Ensure it's bundled with the app.")
    exit(1)

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
                result = subprocess.run([ANTIWORD_PATH, file_path],encoding='windows-1252', capture_output=True, text=True)
                text = result.stdout
                
                if keyword.lower() in text.lower():
                    matching_files.append(filename)
                    shutil.move(file_path, os.path.join(output_folder, filename))
            
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return matching_files, output_folder 

def browse_directory():
    folder_selected = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, folder_selected)

def start_search():
    directory = directory_entry.get()
    keyword = keyword_entry.get()
    output_folder = output_entry.get()

    if not directory or not keyword:
        messagebox.showerror("Error", "Directory and Keyword are required fields!")
        return

    matching_files, output_folder_path = search_and_move_docs(directory, keyword, output_folder)

    result_text_widget.config(state=tk.NORMAL)
    result_text_widget.delete("1.0", tk.END)
    
    if matching_files:
        result_text_widget.insert(
            tk.END,
            f"Moved {len(matching_files)} files to '{output_folder_path}':\n" + "\n".join(matching_files)
        )
    else:
        result_text_widget.insert(tk.END, "No matching files found.")
    
    result_text_widget.config(state=tk.DISABLED)

def on_mousewheel(event):
    result_text_widget.yview_scroll(int(-1*(event.delta/120)), "units")

root = tk.Tk()
root.title("Doc Filter")
root.configure(padx=20, pady=20)

tk.Label(root, text="Directory: *").grid(row=0, column=0, sticky="w")
directory_entry = tk.Entry(root, width=40)
directory_entry.grid(row=0, column=1)
browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2)

tk.Label(root, text="Keyword: *").grid(row=1, column=0, sticky="w")
keyword_entry = tk.Entry(root, width=40)
keyword_entry.grid(row=1, column=1)

tk.Label(root, text="Output Folder (optional):").grid(row=2, column=0, sticky="w")
output_entry = tk.Entry(root, width=40)
output_entry.grid(row=2, column=1)

search_button = tk.Button(root, text="Start Search", command=start_search)
search_button.grid(row=3, column=0, columnspan=2, sticky="e", pady=(10, 10))

result_frame = tk.Frame(root)
result_frame.grid(row=4, column=1, sticky="nsew")

result_text_widget = tk.Text(result_frame, wrap="word", width=50, height=10)
result_text_widget.pack(side="left", fill="both", expand=True)
result_text_widget.config(state=tk.DISABLED)

result_text_widget.bind("<MouseWheel>", on_mousewheel)

root.mainloop()
