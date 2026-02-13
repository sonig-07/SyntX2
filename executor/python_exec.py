
import subprocess
import os
import uuid

TEMP_DIR = "temp"

def run_python(code):
    file_name = f"{uuid.uuid4().hex}.py"
    file_path = os.path.join(TEMP_DIR, file_name)

    with open(file_path, "w") as f:
        f.write(code)

    result = subprocess.run(
        ["python", file_path],
        capture_output=True,
        text=True,
        timeout=5
    )

    return result.stdout + result.stderr
