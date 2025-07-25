import getpass
import os
import hashlib
import json
from ensure_unlocked import ensure_unlocked

def init():
    print(r"""
██╗  ██╗███████╗██╗   ██╗██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗
██║ ██╔╝██╔════╝╚██╗ ██╔╝██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝
█████╔╝ █████╗   ╚████╔╝ ██║   ██║███████║██║   ██║██║     ██║   
██╔═██╗ ██╔══╝    ╚██╔╝  ╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║   
██║  ██╗███████╗   ██║    ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║   
╚═╝  ╚═╝╚══════╝   ╚═╝     ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝   
                                                                 

         🔐 Welcome to KeyVault 🔐
   Your digital secrets. Fortified. 🔒✨
""")

    pw_1 = getpass.getpass("Enter your pw: ")
    pw_confirm = getpass.getpass("Enter again pw: ")

    if pw_1 != pw_confirm:
        print("\n❌ Oops! Passwords don't match. Try again.\n")
        pw_1 = ""
        pw_confirm = ""
        init()

    salt = os.urandom(16)
    combined = str(salt) + pw_1

    hashed = hashlib.sha256(combined.encode())

    vault_data = {
        "user": {
            "salt": str(salt),
            "user_pw": hashed.hexdigest()
        },
        "vault": {}  
    }
    
    with open("vault.json", "w") as file:
        json.dump(vault_data, file, indent=4)

    with open(".lock", "w") as f:
        f.write("locked")

def add():
    ensure_unlocked()
    print("\n🔐 Let's add a new service to your vault\n")

    service = input("🔹 Service name (e.g., GitHub, Gmail): ").strip()
    username = input("🔹 Username / Email: ").strip()
    pw = getpass.getpass("🔸 Password (input hidden): ")

    print("\n📂 Opening your vault...\n")

    with open("vault.json", "r") as f:
        data = json.load(f)

    salt = os.urandom(16)
    combined = str(salt) + pw

    hashed = hashlib.sha256(combined.encode())

    data["vault"][service] = {
        "username": username,
        "pw": hashed.hexdigest()
    }

    with open("vault.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"\n✅ Successfully added '{service.upper()}' to your vault.\n")


