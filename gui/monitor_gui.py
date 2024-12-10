import tkinter as tk
from tkinter import ttk, messagebox
from threading import Thread
from installer.node_monitor import fetch_node_logs, parse_logs, monitor_node_status, start_node, stop_node, restart_node

class NodeMonitorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorand Node Monitor")
        self.root.geometry("1000x700")  # Adjusted size for better visibility
        self.root.minsize(800, 600)

        # Title Label
        tk.Label(self.root, text="Algorand Node Monitoring", font=("Arial", 18)).pack(pady=10)

        # Node Status Frame
        self.status_frame = tk.LabelFrame(self.root, text="Node Status", font=("Arial", 14))
        self.status_frame.pack(fill="x", padx=10, pady=5)

        self.status_tree = ttk.Treeview(self.status_frame, columns=("Property", "Value"), show="headings", height=5)
        self.status_tree.heading("Property", text="Property")
        self.status_tree.heading("Value", text="Value")
        self.status_tree.column("Property", width=300)
        self.status_tree.column("Value", width=600)
        self.status_tree.pack(fill="both", expand=True, padx=10, pady=5)

        # Logs Frame
        self.logs_frame = tk.LabelFrame(self.root, text="Node Logs", font=("Arial", 14))
        self.logs_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.logs_tree = ttk.Treeview(self.logs_frame, columns=("Time", "Level", "Message"), show="headings")
        self.logs_tree.heading("Time", text="Time")
        self.logs_tree.heading("Level", text="Level")
        self.logs_tree.heading("Message", text="Message")
        self.logs_tree.column("Time", width=150)
        self.logs_tree.column("Level", width=100)
        self.logs_tree.column("Message", width=700)
        self.logs_tree.pack(side="left", fill="both", expand=True)

        self.logs_scrollbar = ttk.Scrollbar(self.logs_frame, orient="vertical", command=self.logs_tree.yview)
        self.logs_scrollbar.pack(side="right", fill="y")
        self.logs_tree.configure(yscrollcommand=self.logs_scrollbar.set)

        # Buttons Frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(fill="x", padx=10, pady=10)

        tk.Button(self.buttons_frame, text="Start Node", font=("Arial", 12), command=self.start_node).pack(side="left", padx=10)
        tk.Button(self.buttons_frame, text="Stop Node", font=("Arial", 12), command=self.stop_node).pack(side="left", padx=10)
        tk.Button(self.buttons_frame, text="Restart Node", font=("Arial", 12), command=self.restart_node).pack(side="left", padx=10)
        tk.Button(self.buttons_frame, text="Refresh", font=("Arial", 12), command=self.refresh).pack(side="left", padx=10)
        tk.Button(self.buttons_frame, text="Exit", font=("Arial", 12), command=self.root.quit).pack(side="left", padx=10)

        # Automatically refresh on startup
        self.refresh()

    def refresh(self):
        Thread(target=self.update_status, daemon=True).start()
        Thread(target=self.update_logs, daemon=True).start()

    def update_status(self):
        try:
            status = monitor_node_status()
            self.status_tree.delete(*self.status_tree.get_children())  # Clear current status
            for key, value in status.items():
                self.status_tree.insert("", "end", values=(key, value))
        except Exception as e:
            self.status_tree.delete(*self.status_tree.get_children())
            self.status_tree.insert("", "end", values=("Error", f"Failed to fetch status: {e}"))
            messagebox.showerror("Error", f"Failed to fetch node status: {e}")

    def update_logs(self):
        try:
            logs = fetch_node_logs()
            parsed_logs = parse_logs(logs)
            self.logs_tree.delete(*self.logs_tree.get_children())  # Clear logs
            for log in parsed_logs:
                self.logs_tree.insert("", "end", values=log)
        except Exception as e:
            self.logs_tree.delete(*self.logs_tree.get_children())
            self.logs_tree.insert("", "end", values=("Error", "Error", f"Failed to fetch logs: {e}"))
            messagebox.showerror("Error", f"Failed to fetch logs: {e}")

    def start_node(self):
        try:
            start_node()
            messagebox.showinfo("Success", "Node started successfully!")
            self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start node: {e}")

    def stop_node(self):
        try:
            stop_node()
            messagebox.showinfo("Success", "Node stopped successfully!")
            self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop node: {e}")

    def restart_node(self):
        try:
            restart_node()
            messagebox.showinfo("Success", "Node restarted successfully!")
            self.refresh()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to restart node: {e}")


# For standalone testing
if __name__ == "__main__":
    root = tk.Tk()
    app = NodeMonitorGUI(root)
    root.mainloop()
