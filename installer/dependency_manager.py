import subprocess
import sys

def ensure_dependencies():
    """Ensure required dependencies are installed."""
    dependencies = [
        "python3",
        "python3-tk",
        "curl",
        "gnupg2",
        "software-properties-common",
        "lsb-release",
    ]
    try:
        subprocess.run("apt-get update -y", shell=True, check=True)
        subprocess.run(
            f"apt-get install -y {' '.join(dependencies)}",
            shell=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error during dependency installation: {e}")
        sys.exit(1)
