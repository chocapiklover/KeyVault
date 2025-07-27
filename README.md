````md
# 🔐 KeyVault  
**Your mind forgets. KeyVault doesn’t.**  
_The offline, terminal-first password manager with memory like a vault._

---

## ✨ What is this?

KeyVault is a fully local, command-line password manager built with Python.  
No cloud. No bloat. Just fast, encrypted, offline credential storage.  

We built it because we wanted something _simple, secure_, and _ours_ — a tool for people who live in the terminal and want full control over their secrets.

---

## 🔑 Features

- 🔐 **Per-entry Fernet encryption**
- 🧠 **Session-based auto-lock** after inactivity
- ✅ **Password strength validator**
- 📋 **Add / Get / Update / Delete / List** credentials
- 💾 **Local-first**: all data saved in JSON
- 🧪 **Built for the terminal** — no GUI, no sync

---

## 🚀 Usage

### 1. Clone & install dependencies

```bash
git clone https://github.com/your-username/keyvault
cd keyvault
uv venv
uv pip install -r requirements.txt
````

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
```

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

## 🛠️ Built With

* Python 3.13
* `cryptography.Fernet`
* `hashlib`, `base64`, `getpass`
* `time`, `os`, `json`
* Terminal-first mindset

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

* **GitHub**: [
* **Post**: 
* **Title**: KeyVault
* **Description**: A fully offline password manager with session-based auto-lock and per-entry encryption. Built for the terminal.

> *Made with ❤️ by \ Alex Harmuth & David Nguyen during the **Boot.dev Hackathon 2025***
> \#bootdev #hackathon #python #cli #security

