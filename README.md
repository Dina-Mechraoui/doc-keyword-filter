# **Doc Keyword Filter**

## **Overview**

**Doc Keyword Filter** is a Python script designed to efficiently scan multiple `.doc` files in a specified directory, identify those containing a given keyword, and move the matching files to a designated folder. This tool is particularly useful for organizing large collections of Microsoft Word documents.

## **Features**
- **Bulk Processing** – Scans multiple `.doc` files at once.
- **Keyword Search** – Searches for a specified keyword (case-insensitive).
- **Automated File Management** – Moves matching files to a new directory.
- **Customizable Output Folder** – Allows specifying a custom folder name.
- **Optimized for macOS** – Utilizes `antiword` for efficient document parsing.
- **Designed for Large Collections** – Handles large volumes of documents effectively.

## **Installation**
### **Prerequisites**
Ensure you have the following installed on your system:
1. **Python 3.x**  
   Install Python using Homebrew (if not already installed):  
   ```bash
   brew install python
   ```
2. **Antiword** (Required for `.doc` file processing)  
   Install Antiword using Homebrew:  
   ```bash
   brew install antiword
   ```

## **Usage**
1. **Place** all `.doc` files in a directory of your choice.
2. **Open** a terminal and navigate to the directory where the script is located.
3. **Run** the script using the following command:
   ```bash
   python script.py --directory /path/to/folder --keyword "search_term"
   ```
4. **(Optional)** Specify a custom output folder name:
   ```bash
   python script.py --directory /path/to/folder --keyword "search_term" --output "custom_folder_name"
   ```
5. The script will scan all `.doc` files in the specified directory.
6. Any file containing the keyword will be moved to the output directory within the same directory.

## **Future Improvements**
- Extend support to `.docx` files.
- Expand compatibility to Windows and Linux.

## **🤝 Contributing**
Contributions are welcome! 🎉 If you'd like to suggest improvements, report issues, or contribute code, please feel free to **open an issue** or **submit a pull request**.
