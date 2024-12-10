import tkinter as tk
from tkinter import scrolledtext
import threading
import time
from monitor.node_control import start_node, stop_node, reset_node
from monitor.status_logs import fetch_node_status, fetch_logs

def update_status_and_logs(status_label, log_text_widget):
    """
    Periodically update the node status and fetch logs in the GUI.
    """
    while True:
        # Update status
        status = fetch_node_status()
        status_label.config(text=status)

        # Fetch and display logs
        logs = fetch_logs()
        print(f"Logs to display: {logs}")  # Debugging
        log_text_widget.config(state=tk.NORMAL)  # Allow modifications
        log_text_widget.delete(1.0, tk.END)
        log_text_widget.insert(tk.END, logs)
        log_text_widget.config(state=tk.DISABLED)  # Prevent manual editing

        time.sleep(5)  # Refresh every 5 seconds

def launch_gui():
    """
    Launch the GUI for monitoring the Algorand node.
    """
    root = tk.Tk()
    root.title("Algorand Node Monitor")
    root.geometry("800x600")

    # Title
    title_label = tk.Label(root, text="Algorand Node Monitor", font=("Arial", 18))
    title_label.pack(pady=10)

    # Status label
    status_label = tk.Label(root, text="Fetching node status...", font=("Courier", 12), justify="left", anchor="w")
    status_label.pack(fill=tk.BOTH, expand=True, pady=10)

    # Logs text widget
    log_text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, font=("Courier", 10))
    log_text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    log_text_widget.insert(tk.END, "Fetching logs...")
    log_text_widget.config(state=tk.DISABLED)  # Make logs read-only

    # Buttons frame
    buttons_frame = tk.Frame(root, padx=10, pady=10)
    buttons_frame.pack()

    # Start button
    start_button = tk.Button(buttons_frame, text="Start Node", font=("Arial", 12), command=start_node)
    start_button.grid(row=0, column=0, padx=10, pady=5)

    # Stop button
    stop_button = tk.Button(buttons_frame, text="Stop Node", font=("Arial", 12), command=stop_node)
    stop_button.grid(row=0, column=1, padx=10, pady=5)

    # Reset button
    reset_button = tk.Button(buttons_frame, text="Reset Node", font=("Arial", 12), command=reset_node)
    reset_button.grid(row=0, column=2, padx=10, pady=5)

    # Close button
    close_button = tk.Button(root, text="Close", font=("Arial", 12), command=root.destroy)
    close_button.pack(pady=10)

    # Start background thread for status and logs
    threading.Thread(target=update_status_and_logs, args=(status_label, log_text_widget), daemon=True).start()

    # Run the GUI
    root.mainloop()

if __name__ == "__main__":
    launch_gui()
