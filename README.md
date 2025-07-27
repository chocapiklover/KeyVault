# 🔐 KeyVault

**Your mind forgets. KeyVault doesn’t.**
*The offline, terminal-first password manager with memory like a vault.*

---

## ✨ What is this?

KeyVault is a fully local, command-line password manager built with Python.
No cloud. No bloat. Just fast, encrypted, offline credential storage.

We built it because we wanted something *simple, secure*, and *ours* — a tool for people who live in the terminal and want full control over their secrets.

---

## 🔑 Features

* 🔐 **Per-entry Fernet encryption**
* 🧠 **Session-based auto-lock** after inactivity
* ✅ **Password strength validator**
* 📋 **Add / Get / Update / Delete / List** credentials
* 💾 **Local-first**: all data saved in JSON
* 🧪 **Built for the terminal** — no GUI, no sync

---

## 🚀 Usage
🚀 Getting Started
To run this project locally:

### 1. Clone & install dependencies

```bash
git clone https://github.com/chocapiklover/KeyVault
cd keyvault
uv venv
uv pip install --all
source .venv/bin/activate
uv sync
```

☝️ Make sure uv is installed globally:
curl -LsSf https://astral.sh/uv/install.sh | sh

### 2. Commands

```bash
python main.py init                # Create vault
python main.py unlock             # Unlock vault
python main.py add                # Add credentials
python main.py get <service>      # Retrieve credentials
python main.py update <service>   # Update entry
python main.py delete <service>   # Delete entry
python main.py list               # List all saved services
python main.py lock               # Lock the vault
```

Optional:

```bash
python main.py unlock --no-autolock  # Disable auto-lock for this session
python main.py unlock --hint         # hint for master pass
python main.py get <service> --copy  # Retrieve credentials and copy to clipboard

---

## 🧾 Example vault entry

```json
"vault": {
  "github": {
    "username": "your@email.com",
    "token": "base64_encrypted_pw",
    "key": "base64_encoded_fernet_key"
  }
}
```

---

# 🛠️ Built With

* 🐍 Python 3.13 — cutting-edge and clean

* 🔐 cryptography.Fernet — modern symmetric encryption

* 🧠 hashlib, base64, getpass — for secure hashing & password handling

* ⏱️ time, os, json — lightweight, file-based vault control

* 🖥️ pyperclip — optional clipboard magic for smoother UX

* 🧪 Terminal-first design — no GUI, just you and your vault
---

## 💭 Why we built it

We wanted a password manager that felt like *ours*.
No trackers, no login, no hidden logic — just encryption, stored locally, protected by your master password.

KeyVault is a project with heart.
Minimalist by design. Private by default.
Every entry is encrypted individually, and sessions expire automatically.

---

## ⚠️ Disclaimer

KeyVault was built in just **4 days** during the **Boot.dev Hackathon 2025**.
It’s a working prototype, not production-grade security software.
Use it with care, audit the code, and don't store nuclear launch codes.

---

## 📦 Submission Info

* **GitHub**: [https://github.com/your-username/keyvault](https://github.com/chocapiklover/KeyVault)
* **Post**: 
* **Title**: KeyVault
* **Description**: A fully offline password manager with session-based auto-lock and per-entry encryption. Built for the terminal.

> *Made with ❤️ by Alex Harmuth and David Nguyen during the **Boot.dev Hackathon 2025***
