import subprocess
import unittest

class TestNodeInstaller(unittest.TestCase):
    
    def test_add_algorand_repo(self):
        """Test if the Algorand repository was added successfully."""
        try:
            result = subprocess.run("apt-cache policy algorand", shell=True, stdout=subprocess.PIPE)
            self.assertIn("https://releases.algorand.com/deb/", result.stdout.decode(), "Algorand repo not found")
        except subprocess.CalledProcessError as e:
            self.fail(f"Failed to check Algorand repository: {e}")

    def test_algorand_installed(self):
        """Test if the Algorand node software is installed."""
        try:
            result = subprocess.run("which goal", shell=True, stdout=subprocess.PIPE)
            self.assertTrue(result.stdout, "Algorand node software is not installed")
        except subprocess.CalledProcessError as e:
            self.fail(f"Failed to find goal command: {e}")

    def test_node_start(self):
        """Test if the node can be started."""
        try:
            result = subprocess.run("systemctl status algorand", shell=True, stdout=subprocess.PIPE)
            self.assertIn("active (running)", result.stdout.decode(), "Node did not start")
        except subprocess.CalledProcessError as e:
            self.fail(f"Failed to start Algorand node: {e}")

if __name__ == "__main__":
    unittest.main()

