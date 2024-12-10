import subprocess

def configure_telemetry():
    """Enable telemetry and set the node name."""
    try:
        subprocess.run("diagcfg telemetry enable", shell=True, check=True)
        subprocess.run("diagcfg telemetry name -n $(hostname)", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error configuring telemetry: {e}")
        sys.exit(1)

def update_dns():
    """Update DNS settings and disable DNSSEC."""
    try:
        subprocess.run(
            "echo 'nameserver 8.8.8.8' > /etc/resolv.conf", shell=True, check=True
        )
        subprocess.run(
            "echo '{\"DNSSecurityFlags\": 0}' > /var/lib/algorand/config.json",
            shell=True,
            check=True,
        )
        subprocess.run("systemctl restart algorand", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error updating DNS settings: {e}")
        sys.exit(1)

