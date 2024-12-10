import subprocess

def fetch_node_status():
    """
    Fetch the node's current status using systemctl.
    """
    try:
        result = subprocess.run(
            ["systemctl", "status", "algorand"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if "active (running)" in result.stdout:
            return "Algorand Node is running."
        elif "inactive (dead)" in result.stdout:
            return "Algorand Node is stopped."
        else:
            return "Algorand Node status: Unknown."
    except FileNotFoundError:
        return "Error: systemctl not found or not configured for Algorand."

def fetch_logs():
    """
    Fetch the latest 20 logs for the Algorand service.
    """
    try:
        result = subprocess.run(
            ["sudo", "journalctl", "-u", "algorand", "--no-pager", "-n", "20"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print("Fetched batch logs...")  # Debugging
        print(result.stdout)            # Debugging

        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        else:
            return "No new log entries."
    except Exception as e:
        print(f"Error fetching logs: {e}")  # Debugging
        return f"Error fetching logs: {e}"
