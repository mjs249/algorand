import tkinter as tk
from tkinter import messagebox
from installer.node_installer import install_node
from installer.dependency_manager import check_dependencies

def on_close():
    """Handle the close button event."""
    if messagebox.askokcancel("Quit", "Do you want to quit the installer?"):
        root.destroy()

def run_installation(status_label):
    """Run the real installation process and update the GUI."""
    try:
        status_label.config(text="Status: Checking Dependencies...")
        root.update()  # Force GUI to update

        check_dependencies()

        status_label.config(text="Status: Installing Algorand Node...")
        root.update()  # Force GUI to update

        install_node()

        status_label.config(text="Status: Installation Complete!")
        messagebox.showinfo("Success", "Algorand node installation completed successfully!")

    except Exception as e:
        status_label.config(text="Status: Installation Failed")
        messagebox.showerror("Error", f"An error occurred: {e}")

def launch_gui():
    """Launch the GUI for the Algorand installer."""
    global root
    root = tk.Tk()
    root.title("Algorand Installer")
    root.geometry("500x300")

    # Create a label
    title_label = tk.Label(root, text="Algorand Node Installer", font=("Arial", 16))
    title_label.pack(pady=20)

    # Create a status label
    status_label = tk.Label(root, text="Status: Ready", font=("Arial", 12))
    status_label.pack(pady=10)

    # Create an install button
    install_button = tk.Button(
        root,
        text="Start Installation",
        command=lambda: run_installation(status_label),
        font=("Arial", 12)
    )
    install_button.pack(pady=20)

    # Create a close button
    close_button = tk.Button(root, text="Close", command=on_close, font=("Arial", 12))
    close_button.pack(pady=10)

    # Run the GUI event loop
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
