import subprocess
import unittest

class TestNodeMonitor(unittest.TestCase):
    
    def test_node_status(self):
        """Test if node status can be checked."""
        try:
            result = subprocess.run("goal node status", shell=True, stdout=subprocess.PIPE)
            self.assertIn("Last committed block", result.stdout.decode(), "Node status retrieval failed")
        except subprocess.CalledProcessError as e:
            self.fail(f"Failed to retrieve node status: {e}")

    def test_monitoring_output(self):
        """Test if the monitoring output is user-friendly."""
        try:
            result = subprocess.run("goal node status | grep 'Last committed block'", shell=True, stdout=subprocess.PIPE)
            self.assertRegex(result.stdout.decode(), r"Last committed block: \d+", "Monitoring output is not in expected format")
        except subprocess.CalledProcessError as e:
            self.fail(f"Failed to verify monitoring output: {e}")

if __name__ == "__main__":
    unittest.main()

