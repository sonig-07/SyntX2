# ⚡SyntX – Multi-Language Code Execution Platform

SyntX is a web-based multi-language code execution platform that allows users to write and execute **Java, Python, and JavaScript** programs from a single interface.

It simulates the core functionality of online coding platforms by handling runtime execution, structured error reporting, and execution time measurement.

---

## 🚀 Features

- 🌐 Multi-language support (Java, Python, JavaScript)
- ⚡ Real-time code execution
- ⏱ Execution time measurement
- 🛑 Timeout protection for infinite loops
- 🎨 Syntax-highlighted editor
- 📁 File upload support

---

## 🛠 Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

---

## 🧠 How It Works

1. User selects a programming language.
2. Code is sent to the Flask backend via REST API.
3. Backend creates a temporary file (`.py`, `.java`, `.js`).
4. Using `subprocess.run()`, the appropriate compiler/runtime is executed:
   - Python → `python`
   - Java → `javac` + `java`
   - JavaScript → `node`
5. Output, errors, and execution time are captured and returned to the frontend.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sonig-07/SyntX2.git
cd SyntX2
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Open in Browser

```
http://localhost:8080
```

---

## 🎯 Learning Outcomes

This project helped in understanding:

- Runtime execution flow
- Compiler vs interpreter delegation
- Process management using subprocess
- Timeout handling and safe execution
- Frontend–backend integration

---

## 👨‍💻 Author

**Soni G**  
GitHub: https://github.com/sonig-07
