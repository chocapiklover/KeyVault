import json
from app.ensure_unlocked import ensure_unlocked
from cryptography.fernet import Fernet
from app.validate_pw import validate_pw
from app.session_valid import session_valid
from app.pw_generate import random_pw_generator

def list():
    ensure_unlocked()
    session_valid()

    with open("vault.json", "r") as f:
        data = json.load(f)

    print("\n🗂️  Stored Services")
    print("────────────────────────")

    if not data["vault"]:
        print("❌ No services saved yet.")
    else:
        for service in data["vault"]:
            print(f"🔐 {service}")

    print("────────────────────────\n")