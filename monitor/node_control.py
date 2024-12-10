import subprocess
from tkinter import messagebox

def start_node():
    try:
        subprocess.run(["sudo", "systemctl", "start", "algorand"], check=True)
        messagebox.showinfo("Start Node", "Algorand node started successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to start node: {e}")

def stop_node():
    try:
        subprocess.run(["sudo", "systemctl", "stop", "algorand"], check=True)
        messagebox.showinfo("Stop Node", "Algorand node stopped successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to stop node: {e}")

def reset_node():
    try:
        subprocess.run(["sudo", "systemctl", "restart", "algorand"], check=True)
        messagebox.showinfo("Reset Node", "Algorand node reset successfully.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to reset node: {e}")
