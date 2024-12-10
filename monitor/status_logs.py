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
    Fetch the latest filtered logs for the Algorand service using journalctl.
    """
    try:
        # Fetch the latest 20 logs
        result = subprocess.run(
            ["journalctl", "-u", "algorand", "--no-pager", "-n", "20"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0 and result.stdout.strip():
            logs = result.stdout.strip()
            
            # Filter out overly verbose lines
            filtered_logs = "\n".join(
                line for line in logs.split("\n")
                if not line.startswith("Config loaded") and not line.startswith("{")
            )
            
            return filtered_logs if filtered_logs else "No relevant log entries found."
        else:
            return f"Error fetching logs: {result.stderr.strip()}"
    except FileNotFoundError:
        return "Error: journalctl not found or not configured for Algorand."

