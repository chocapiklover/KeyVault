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
                                                                    

            🔐 Lets create your KeyVault 🔐
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


def unlock():
    pw = getpass.getpass("Enter your pw: ")

    with open("vault.json", "r") as file:
        vault_data = json.load(file)

        hashed_from_file = vault_data["user"]["user_pw"]
        salt_from_file = vault_data["user"]["salt"]

        combined = str(salt_from_file) + pw
        hashed = hashlib.sha256(combined.encode())

        if hashed.hexdigest() == hashed_from_file:
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
            os.remove(".lock")
        else:
            print("❌ Unlock failed.")


def lock():
    if os.path.exists(".lock"):
        print("Vault is already locked.")
    else:
        with open(".lock", "w") as f:
            f.write("locked")
        print("🔒 Vault is now locked.")


def list():
    ensure_unlocked()
    
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
