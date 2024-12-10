# installer/privilege_manager.py

import os
import sys  # Import sys module

def check_and_add_sudo():
    """Check if the current user has sudo privileges, if not, add them."""
    if os.geteuid() != 0:
        print("This script needs root privileges to run.")
        try:
            root_password = input("Please enter the root password: ")
            # Re-run the script with root privileges
            os.execvp("su", ["su", "-c", f"python3 {' '.join(sys.argv)}"])
        except Exception as e:
            print(f"Failed to escalate privileges: {e}")
            sys.exit(1)  # Ensure sys.exit() is called after importing sys

def add_user_to_sudo():
    """Add the current user to the sudoers group."""
    try:
        # Get the current username
        username = os.getlogin()
        # Check if the user is already in the sudo group
        if username not in os.popen("groups").read():
            print(f"Adding {username} to sudo group...")
            # Add the user to the sudo group
            os.system(f"sudo usermod -aG sudo {username}")
            print(f"{username} has been added to the sudo group.")
        else:
            print(f"{username} is already in the sudo group.")
    except Exception as e:
        print(f"Error while adding the user to sudo group: {e}")
        sys.exit(1)
