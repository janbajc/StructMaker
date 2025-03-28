# StructMaker

StructMaker is a simple Python tool that generates folder structures from text input, supporting nested subfolders. It works on both Windows and Linux, making it easy to set up project directories quickly.

## Features
- Create folders and files from text input
- Supports nested subfolders with indentation
- Works on Windows and Linux
- Customizable base folder name

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/StructMaker.git
   cd StructMaker
   ```

2. (Optional) Create a virtual environment:
   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/macOS: `source venv/bin/activate`

## Usage
1. Run the script:
   ```sh
   python struct_maker.py
   ```
2. Paste the folder structure (e.g.):
   ```
   /my_project
   │── /src
   │   ├── /utils
   │── /tests
   │── README.md
   END
   ```
3. Enter the base folder name (or leave blank for the current directory).
4. The tool will create the structure for you.

## Example Output
```
my_project/
├── src/
│   ├── utils/
├── tests/
├── README.md
```

## License
MIT License.

## Contributing
PRs are welcome!