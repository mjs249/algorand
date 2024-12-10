import subprocess

def is_dependency_installed(dependency):
    """
    Check if a system dependency is installed.
    Returns True if the dependency is found, False otherwise.
    """
    try:
        subprocess.run(
            ["which", dependency],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

def install_dependency(dependency):
    """
    Install a specific system dependency using apt-get.
    Assumes the script is running with sudo privileges.
    """
    print(f"Installing {dependency}...")
    try:
        subprocess.run(
            ["sudo", "apt-get", "install", "-y", dependency],
            check=True
        )
        print(f"Successfully installed {dependency}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {dependency}: {e}")
        raise

def check_dependencies():
    """
    Check and install all required dependencies for the project.
    """
    dependencies = ["curl", "tar", "python3-venv"]  # Add other required dependencies here
    print("Checking system dependencies...")

    for dep in dependencies:
        if not is_dependency_installed(dep):
            print(f"{dep} is not installed.")
            install_dependency(dep)
        else:
            print(f"{dep} is already installed.")

    print("All dependencies are installed.")

if __name__ == "__main__":
    # Run dependency checks directly for testing purposes
    check_dependencies()
