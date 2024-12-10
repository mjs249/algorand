import subprocess
from tkinter import messagebox

def start_node():
    """
    Start the Algorand node using systemctl.
    """
    try:
        subprocess.run(["sudo", "systemctl", "start", "algorand"], check=True)
        messagebox.showinfo("Start Node", "Algorand node started successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to start node: {e}")
    except FileNotFoundError:
        messagebox.showerror("Error", "systemctl not found or not configured for Algorand.")

def stop_node():
    """
    Stop the Algorand node using systemctl.
    """
    try:
        subprocess.run(["sudo", "systemctl", "stop", "algorand"], check=True)
        messagebox.showinfo("Stop Node", "Algorand node stopped successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to stop node: {e}")
    except FileNotFoundError:
        messagebox.showerror("Error", "systemctl not found or not configured for Algorand.")

def reset_node():
    """
    Restart the Algorand node using systemctl.
    """
    try:
        subprocess.run(["sudo", "systemctl", "restart", "algorand"], check=True)
        messagebox.showinfo("Reset Node", "Algorand node reset successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to reset node: {e}")
    except FileNotFoundError:
        messagebox.showerror("Error", "systemctl not found or not configured for Algorand.")
