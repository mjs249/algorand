import subprocess

def install_algorand_node():
    """Perform the steps to install the Algorand node."""
    commands = [
        "curl -o - https://releases.algorand.com/key.pub | tee /etc/apt/trusted.gpg.d/algorand.asc",
        "add-apt-repository -y 'deb [arch=amd64] https://releases.algorand.com/deb/ stable main'",
        "apt-get install -y algorand algorand-devtools",
        "systemctl start algorand",
    ]
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Installation step failed: {e}")
            sys.exit(1)
