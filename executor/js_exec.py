
import subprocess
import os
import uuid

TEMP_DIR = "temp"

def run_js(code):
    file_name = f"{uuid.uuid4().hex}.js"
    file_path = os.path.join(TEMP_DIR, file_name)

    with open(file_path, "w") as f:
        f.write(code)

    result = subprocess.run(
        ["node", file_path],
        capture_output=True,
        text=True,
        timeout=5
    )

    return result.stdout + result.stderr
