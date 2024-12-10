import subprocess
import unittest

class TestDependencyManager(unittest.TestCase):
    
    def test_dependency_installation(self):
        """Test if the required dependencies are installed correctly."""
        # Check if python3 and required packages are installed
        try:
            subprocess.run("dpkg -l | grep python3", shell=True, check=True, stdout=subprocess.PIPE)
            subprocess.run("dpkg -l | grep curl", shell=True, check=True, stdout=subprocess.PIPE)
            subprocess.run("dpkg -l | grep gnupg2", shell=True, check=True, stdout=subprocess.PIPE)
            subprocess.run("dpkg -l | grep software-properties-common", shell=True, check=True, stdout=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            self.fail(f"Dependencies were not installed correctly: {e}")

if __name__ == "__main__":
    unittest.main()

