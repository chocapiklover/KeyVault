import getpass
import os
import hashlib
import json

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

def unlock():
    pw = getpass.getpass("Enter your pw: ")

    with open("vault.json", "r") as file:
        vault_data = json.load(file)

        hashed_from_file = vault_data["user"]["user_pw"]
        salt_from_file = vault_data["user"]["salt"]

        combined = str(salt_from_file) + pw
        hashed = hashlib.sha256(combined.encode())

        if hashed.hexdigest() == hashed_from_file:
            print("✅ Unlock successful!")
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
