from installer.node_installer import install_node
from installer.dependency_manager import check_dependencies
from installer.installer_gui import launch_gui

def main():
    """
    Main entry point for the Algorand installer.
    This function integrates the installation logic with a GUI.
    """
    print("Starting the Algorand installer...")
    try:
        # Launch the GUI to handle the installation
        launch_gui()
    except Exception as e:
        print(f"An error occurred during the installation process: {e}")

if __name__ == "__main__":
    main()

