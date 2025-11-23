import os
from pathlib import Path

def create_file(path, content=""):
    """Create a file with the given content"""
    # Fix for Windows paths - handle root level files
    dir_name = os.path.dirname(path)
    if dir_name and dir_name != path:  # Only create dirs if needed and not root level
        os.makedirs(dir_name, exist_ok=True)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_project_structure():
    """Create the AI Data Analyst Agent project structure"""
    
    # Define the project structure
    project_structure = {
        "requirements.txt": "",
        "README.md": "",
        
        "data/sample_sales.csv": "",
        "data/init_db.py": "",
        
        "app/main.py": "",
        "app/config.py": "",
        "app/db.py": "",
        "app/schemas.py": "",
        
        "app/services/__init__.py": "",
        "app/services/nl2sql.py": "",
        "app/services/analysis.py": "",
        
        "app/static/plots/.gitkeep": "",
        "app/static/index.html": "",
    }
    
    # Create all files
    for file_path, content in project_structure.items():
        create_file(file_path, content)
    
    print("✅ AI Data Analyst Agent project structure created successfully!")
    print("📁 ai-data-analyst-agent/")
    print("│  requirements.txt")
    print("│  README.md")
    print("│")
    print("├─ data/")
    print("│   sample_sales.csv")
    print("│   init_db.py")
    print("│")
    print("├─ app/")
    print("│   main.py")
    print("│   config.py")
    print("│   db.py")
    print("│   schemas.py")
    print("│")
    print("│   ├─ services/")
    print("│   │    __init__.py")
    print("│   │    nl2sql.py")
    print("│   │    analysis.py")
    print("│   │")
    print("│   └─ static/")
    print("│        plots/        # generated charts")
    print("│        index.html    # minimal frontend UI")

if __name__ == "__main__":
    create_project_structure()
