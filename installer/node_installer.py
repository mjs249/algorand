import os
import subprocess

def check_root():
    """Ensure the script is running with root privileges."""
    if os.geteuid() != 0:
        raise PermissionError("This script must be run as root. Please use sudo.")

def install_dependencies():
    """Install required system dependencies for the Algorand node."""
    dependencies = ["curl", "tar"]
    print("Checking and installing dependencies...")
    for dep in dependencies:
        print(f"Ensuring {dep} is installed...")
        subprocess.run(["sudo", "apt-get", "install", "-y", dep], check=True)

def download_algorand_node():
    """Download the Algorand node installation script."""
    url = "https://raw.githubusercontent.com/algorand/go-algorand-doc/master/downloads/installers/update.sh"
    print("Downloading Algorand node installation script...")
    subprocess.run(["curl", "-O", url], check=True)
    subprocess.run(["chmod", "+x", "update.sh"], check=True)

def install_algorand_node():
    """Run the installation script for the Algorand node."""
    data_dir = "/var/lib/algorand"  # Replace with your preferred data directory
    print("Running Algorand node installation script...")
    subprocess.run(["./update.sh", "-i", "-c", "-p", "-d", data_dir], check=True)

def clean_up():
    """Clean up temporary files."""
    if os.path.exists("update.sh"):
        os.remove("update.sh")
        print("Removed temporary installation script.")

def install_node():
    """
    Main function to install the Algorand node.
    - Ensures root privileges.
    - Installs dependencies.
    - Downloads and installs the Algorand node.
    - Cleans up temporary files.
    """
    try:
        print("Starting Algorand node installation...")
        check_root()
        install_dependencies()
        download_algorand_node()
        install_algorand_node()
        print("Algorand node installation complete!")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    finally:
        clean_up()
