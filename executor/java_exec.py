
import subprocess
import os

TEMP_DIR = "temp"

def run_java(code):
    file_path = os.path.join(TEMP_DIR, "Main.java")

    with open(file_path, "w") as f:
        f.write(code)

    compile_process = subprocess.run(
        ["javac", file_path],
        capture_output=True,
        text=True,
        timeout=5
    )

    if compile_process.stderr:
        return compile_process.stderr

    run_process = subprocess.run(
        ["java", "-cp", TEMP_DIR, "Main"],
        capture_output=True,
        text=True,
        timeout=5
    )

    return run_process.stdout + run_process.stderr
