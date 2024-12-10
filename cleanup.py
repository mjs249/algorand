import os
import shutil

# List of directories and files to remove
UNNECESSARY_PATHS = [
    "build", "dist", "__pycache__", "*.pyc", "main.spec"
]

# Function to delete unnecessary files and directories
def delete_unnecessary_paths(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Delete unnecessary directories
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            if any(phrase in full_path for phrase in UNNECESSARY_PATHS):
                shutil.rmtree(full_path)
                print(f"Deleted directory: {full_path}")
        # Delete unnecessary files
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if any(full_path.endswith(pattern) for pattern in UNNECESSARY_PATHS):
                os.remove(full_path)
                print(f"Deleted file: {full_path}")

# Function to reorganize the remaining files
def reorganize_project(root_dir):
    # Ensure essential directories exist
    essential_dirs = ["installer", "gui", "tests"]
    for essential_dir in essential_dirs:
        dir_path = os.path.join(root_dir, essential_dir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Created directory: {dir_path}")
    
    # Move essential files if they're in the root directory
    file_map = {
        "installer/": ["dependency_manager.py", "node_installer.py", "node_monitor.py", "privilege_manager.py", "telemetry_config.py"],
        "gui/": ["installer_gui.py", "monitor_gui.py"],
        "tests/": ["test_dependencies.py", "test_installation.py", "test_monitor.py", "test_privileges.py"],
    }

    for dest_dir, files in file_map.items():
        for file in files:
            src_path = os.path.join(root_dir, file)
            dest_path = os.path.join(root_dir, dest_dir, file)
            if os.path.exists(src_path):
                shutil.move(src_path, dest_path)
                print(f"Moved {src_path} to {dest_path}")

# Main cleanup function
def main():
    project_root = "/mnt/data/algorand-main"  # Adjust to your project path
    print("Cleaning up unnecessary files...")
    delete_unnecessary_paths(project_root)
    print("Reorganizing project structure...")
    reorganize_project(project_root)
    print("Cleanup and reorganization complete!")

if __name__ == "__main__":
    main()
