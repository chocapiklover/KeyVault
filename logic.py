import getpass
import os
import hashlib
import json

def logic():
    print("Salam")

    pw_1 = getpass.getpass("Enter your pw: ")
    pw_confirm = getpass.getpass("Enter again pw: ")

    if pw_1 != pw_confirm:
        pw_1 = ""
        pw_confirm = ""
        logic()

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

