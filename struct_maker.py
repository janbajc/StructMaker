import os

def create_structure_from_text(structure_text, base_path="."):
    lines = structure_text.strip().split("\n")
    
    for line in lines:
        line = line.strip()
        if line.startswith("│") or line.startswith("/"):  # Folder
            folder_path = os.path.join(base_path, line.replace("│──", "").replace("/", "").strip())
            os.makedirs(folder_path, exist_ok=True)
            print(f"📂 Created folder: {folder_path}")
        elif "." in line:  # File
            file_path = os.path.join(base_path, line.strip())
            with open(file_path, "w") as f:
                f.write(f"# {file_path}")  # Add default content
            print(f"📄 Created file: {file_path}")

if __name__ == "__main__":
    print("Paste your folder structure below. Type 'END' to finish:")
    
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    structure_text = "\n".join(lines)
    
    base_folder = input("Enter the base folder name (or press Enter for current directory): ").strip()
    base_folder = base_folder if base_folder else "."

    create_structure_from_text(structure_text, base_folder)
