import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import time

def fetch_node_status(data_dir):
    """
    Fetch the node's current status using the `goal node status` command.
    """
    try:
        result = subprocess.run(
            ["goal", "node", "status", "-d", data_dir],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
    except FileNotFoundError:
        return "Error: Algorand tools not installed or not in PATH."

def update_status(status_label, data_dir):
    """
    Periodically update the status in the GUI.
    """
    while True:
        status = fetch_node_status(data_dir)
        status_label.config(text=status)
        time.sleep(5)  # Update every 5 seconds

def launch_monitor_gui():
    """
    Launch the GUI for monitoring the Algorand node.
    """
    data_dir = "/var/lib/algorand"  # Replace with your node's data directory

    # Create the main GUI window
    root = tk.Tk()
    root.title("Algorand Node Monitor")
    root.geometry("600x400")

    # Title label
    title_label = tk.Label(root, text="Algorand Node Monitor", font=("Arial", 18))
    title_label.pack(pady=20)

    # Status label
    status_label = tk.Label(root, text="Fetching node status...", font=("Arial", 12), justify="left")
    status_label.pack(pady=10)

    # Start the status update thread
    threading.Thread(target=update_status, args=(status_label, data_dir), daemon=True).start()

    # Close button
    close_button = tk.Button(root, text="Close", command=root.destroy, font=("Arial", 12))
    close_button.pack(pady=20)

    # Run the GUI event loop
    root.mainloop()
