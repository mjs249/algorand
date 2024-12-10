import tkinter as tk
from tkinter import messagebox
from threading import Thread
from installer.node_installer import install_algorand_node

class AlgorandInstallerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorand Node Installer")
        self.root.geometry("600x400")

        # Title Label
        tk.Label(self.root, text="Algorand Node Installer", font=("Arial", 18)).pack(pady=20)

        # Status Label
        self.status_label = tk.Label(self.root, text="Ready to install.", font=("Arial", 12))
        self.status_label.pack(pady=10)

        # Install Button
        self.install_button = tk.Button(self.root, text="Install Node", font=("Arial", 14), command=self.start_installation)
        self.install_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", font=("Arial", 14), command=self.root.quit)
        self.exit_button.pack(pady=10)

    def start_installation(self):
        """Run the installation in a separate thread."""
        Thread(target=self.run_installation, daemon=True).start()

    def run_installation(self):
        """Perform the node installation."""
        self.status_label.config(text="Installing...")
        try:
            install_algorand_node()
            self.status_label.config(text="Installation complete.")
            messagebox.showinfo("Success", "Algorand Node installed successfully!")
        except Exception as e:
            self.status_label.config(text="Installation failed.")
            messagebox.showerror("Error", f"Installation failed: {e}")
