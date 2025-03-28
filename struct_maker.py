import os

def create_structure_from_text(structure_text, base_path="."):
    lines = structure_text.strip().split("\n")
    stack = [base_path]  # Stack to track nested folder levels

    for line in lines:
        stripped_line = line.lstrip("│ ")  # Remove visual characters
        depth = (len(line) - len(stripped_line)) // 2  # Count indentation levels

        current_path = os.path.join(stack[depth], stripped_line.replace("/", "").strip())

        if "/" in stripped_line or "├──" in line or "│──" in line:  # Folder
            os.makedirs(current_path, exist_ok=True)
            stack = stack[:depth + 1] + [current_path]  # Adjust stack for nesting
            print(f"Created folder: {current_path}")
        else:  # File
            with open(current_path, "w") as f:
                f.write(f"# {current_path}")  # Default content
            print(f"Created file: {current_path}")

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
