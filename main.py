# main.py
# -*- coding: utf-8 -*-
import os
import sys
import tkinter as tk
from installer.privilege_manager import check_and_add_sudo
from installer.node_installer import install_algorand_node
from gui.installer_gui import AlgorandInstallerGUI
from gui.monitor_gui import NodeMonitorGUI

def ensure_dependencies():
    """Ensure that all required dependencies are installed before proceeding."""
    import subprocess
    try:
        print("Checking and installing dependencies...")
        subprocess.run("apt-get update -y", shell=True, check=True)
        subprocess.run("apt-get install -y python3 python3-tk curl gnupg2 software-properties-common lsb-release", shell=True, check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during dependency installation: {e}")
        sys.exit(1)

def run_gui():
    """Run the GUI application."""
    root = tk.Tk()
    root.title("Algorand Installer & Monitor")
    root.geometry("800x600")
    
    def open_installer():
        """Open the installer GUI."""
        installer_gui = tk.Toplevel(root)
        AlgorandInstallerGUI(installer_gui)
    
    def open_monitor():
        """Open the monitor GUI."""
        monitor_gui = tk.Toplevel(root)
        NodeMonitorGUI(monitor_gui)
    
    # Main GUI layout
    tk.Label(root, text="Algorand Node Manager", font=("Arial", 20)).pack(pady=20)
    tk.Button(root, text="Open Installer", font=("Arial", 14), command=open_installer).pack(pady=10)
    tk.Button(root, text="Open Monitor", font=("Arial", 14), command=open_monitor).pack(pady=10)
    tk.Button(root, text="Exit", font=("Arial", 14), command=root.quit).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    try:
        # Ensure root privileges
        check_and_add_sudo()
        
        # Ensure dependencies are installed
        ensure_dependencies()
        
        # Launch GUI
        run_gui()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
