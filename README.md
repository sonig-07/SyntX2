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

## 📸 Screenshots

<img width="927" height="742" alt="Screenshot 2026-02-13 224011" src="https://github.com/user-attachments/assets/19583cf1-c398-4ac6-8123-e6c3b47beaff" />
<img width="1001" height="801" alt="Screenshot 2026-02-13 224024" src="https://github.com/user-attachments/assets/7ecf0fc1-ea16-43d6-9911-698554dead02" />
<img width="1037" height="830" alt="Screenshot 2026-02-13 224034" src="https://github.com/user-attachments/assets/24d7ec74-cf51-463c-8d8c-eb2026278614" />
<img width="1094" height="868" alt="Screenshot 2026-02-13 224339" src="https://github.com/user-attachments/assets/70fbf267-e26d-4e9c-9421-71f2cd252ca9" />

---

## 👨‍💻 Author

**Soni G**  
GitHub: https://github.com/sonig-07
