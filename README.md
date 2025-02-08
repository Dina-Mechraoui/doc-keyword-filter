# Doc Keyword Filter

## Overview

Doc Keyword Filter is a Python script designed to scan multiple `.doc` files in a specified directory, identify those containing a given keyword, and move the matching files to a new folder. It is particularly useful for organizing large collections of Microsoft Word documents efficiently.

---

## Features

- Scans and processes `.doc` files in bulk.
- Searches for a specified keyword (case-insensitive).
- Moves matching files to a newly created directory.
- Optimized for macOS using `antiword`.
- Designed for handling large document collections.

---

## Installation

### Prerequisites

1. **Python 3.x**  
   If Python is not installed, install it using Homebrew:
   brew install python

2. **Antiword (Required for .doc files)**  
   If Python is not installed, install it using Homebrew:
   brew install antiword

---

## Usage

1. Place all .doc files in a directory.
2. Navigate to the directory where the script is located.
3. Add the `directory path`, `keyword` and the `output folder name` to the script.
4. run the script
    python script.py
5. The script will scan all .doc files in the specified directory.
6. Any file containing the keyword will be moved to the output directory within the same directory.

---

## Future Improvements

- Extend support to .docx files.
- Expand compatibility to Windows and Linux.

---

## Contributing

Contributions are welcome. If you would like to suggest improvements or report issues, please open an issue or submit a pull request.