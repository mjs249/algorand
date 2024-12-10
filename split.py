import os
import shutil

# Define paths for splitting and reorganizing
base_path = os.path.expanduser('~/algorand-installer')  # Expanding `~` to the full home directory path
gui_dir = os.path.join(base_path, 'gui')
installer_dir = os.path.join(base_path, 'installer')
monitor_dir = os.path.join(base_path, 'monitor')

# Ensure necessary directories exist
for directory in [installer_dir, monitor_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

# Move `installer_gui.py` from `gui/` to `installer/`
installer_gui_src = os.path.join(gui_dir, 'installer_gui.py')
installer_gui_dest = os.path.join(installer_dir, 'installer_gui.py')
if os.path.exists(installer_gui_src):
    shutil.move(installer_gui_src, installer_gui_dest)
    print(f"Moved {installer_gui_src} to {installer_gui_dest}")

# Create `main.py` for `installer/`
installer_main_path = os.path.join(installer_dir, 'main.py')
with open(installer_main_path, 'w') as f:
    f.write("""\
from node_installer import install_node
from dependency_manager import check_dependencies

def main():
    print("Starting the Algorand installer...")
    check_dependencies()
    install_node()

if __name__ == "__main__":
    main()
""")
    print(f"Created {installer_main_path}")

# Create `main.py` for `monitor/`
monitor_main_path = os.path.join(monitor_dir, 'main.py')
with open(monitor_main_path, 'w') as f:
    f.write("""\
from monitor_gui import launch_monitor_gui

def main():
    print("Starting the Algorand monitor...")
    launch_monitor_gui()

if __name__ == "__main__":
    main()
""")
    print(f"Created {monitor_main_path}")

# Remove the now-empty `gui/` directory if it exists
if os.path.exists(gui_dir):
    shutil.rmtree(gui_dir)
    print(f"Deleted {gui_dir}")

print("Splitting and reorganization complete.")
