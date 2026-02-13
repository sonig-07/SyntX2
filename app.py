from flask import Flask, render_template, request, jsonify
import os
import time

from executor.python_exec import run_python
from executor.java_exec import run_java
from executor.js_exec import run_js

app = Flask(__name__)

# Ensure temp directory exists
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Code execution route
@app.route("/run", methods=["POST"])
def run():
    data = request.json
    language = data.get("language")
    code = data.get("code")

    if not code or not code.strip():
        return jsonify({
            "output": "",
            "error": "No code provided.",
            "execution_time": 0
        })

    start_time = time.time()

    try:
        if language == "python":
            result = run_python(code)
        elif language == "java":
            result = run_java(code)
        elif language == "javascript":
            result = run_js(code)
        else:
            result = "Unsupported language."
    except Exception as e:
        result = str(e)

    end_time = time.time()
    execution_time = round(end_time - start_time, 6)

    # Simple error detection
    if "error" in result.lower():
        return jsonify({
            "output": "",
            "error": result,
            "execution_time": execution_time
        })

    return jsonify({
        "output": result,
        "error": "",
        "execution_time": execution_time
    })


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True, port=8080)
