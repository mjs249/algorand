import subprocess
import unittest

class TestPrivilegeManager(unittest.TestCase):
    
    def test_user_in_sudo_group(self):
        """Test if the user is added to the sudo group."""
        try:
            result = subprocess.run("groups michael", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.assertIn("sudo", result.stdout.decode(), "User is not in the sudo group")
        except subprocess.CalledProcessError as e:
            self.fail(f"Failed to check if user is in sudo group: {e}")

    def test_sudo_password_prompt(self):
        """Test if the root password prompt is correctly triggered."""
        try:
            # Simulate a command that requires sudo privileges
            result = subprocess.run(["sudo", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.assertEqual(result.returncode, 0, "Failed to request sudo password")
        except subprocess.CalledProcessError as e:
            self.fail(f"Sudo password prompt failed: {e}")

if __name__ == "__main__":
    unittest.main()

