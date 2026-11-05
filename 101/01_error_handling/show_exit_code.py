# Helper: runs a script, then shows its exit code (0 = success, 1 = failure)
import subprocess
import sys

script = sys.argv[1]
result = subprocess.run([sys.executable, script])
print("exit code:", result.returncode)
