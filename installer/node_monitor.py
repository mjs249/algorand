import subprocess
import os
import json
import re

def fetch_node_logs(log_file="/var/lib/algorand/node.log"):
    """Fetch the Algorand node logs from the specified log file."""
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            return f.readlines()
    else:
        raise FileNotFoundError(f"Log file {log_file} not found.")

def parse_logs(log_lines):
    """Parse the fetched log lines into structured entries for the GUI table."""
    parsed_logs = []
    for line in log_lines:
        try:
            log_entry = json.loads(line.strip())  # Assuming JSON-formatted logs
            parsed_logs.append((
                log_entry.get("time", "N/A"),
                log_entry.get("level", "N/A"),
                log_entry.get("msg", "N/A")
            ))
        except (json.JSONDecodeError, KeyError):
            # If log is not JSON or lacks expected fields, add it as raw
            parsed_logs.append(("N/A", "N/A", line.strip()))
    return parsed_logs

def monitor_node_status(data_dir="/var/lib/algorand"):
    """Monitor the node status by checking the current status of the node."""
    try:
        command = f"goal node status -d {data_dir}"
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE)
        status_lines = result.stdout.splitlines()
        status_dict = {}
        
        # Extract key-value pairs from the output
        for line in status_lines:
            match = re.match(r"(.+?):\s+(.+)", line)
            if match:
                key, value = match.groups()
                status_dict[key.strip()] = value.strip()
        
        return status_dict
    except subprocess.CalledProcessError as e:
        return {"Error": f"Error fetching node status: {e.stderr}"}

def start_node():
    """Start the Algorand node."""
    try:
        subprocess.run(["systemctl", "start", "algorand"], check=True)
        return "Node started successfully."
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to start the node: {e.stderr}")

def stop_node():
    """Stop the Algorand node."""
    try:
        subprocess.run(["systemctl", "stop", "algorand"], check=True)
        return "Node stopped successfully."
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to stop the node: {e.stderr}")

def restart_node():
    """Restart the Algorand node."""
    try:
        subprocess.run(["systemctl", "restart", "algorand"], check=True)
        return "Node restarted successfully."
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to restart the node: {e.stderr}")
