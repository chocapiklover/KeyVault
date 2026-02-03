import getpass
import os
import hashlib
import json
from app.ensure_unlocked import ensure_unlocked
from cryptography.fernet import Fernet
from app.validate_pw import validate_pw
from app.session_valid import session_valid
import time
from app.pw_generate import random_pw_generator

def unlock(disable = None, hint=False):
    if not os.path.exists(".lock"):
        print("already unlocked!")
        exit(1)

    with open("vault.json", "r") as file:
        vault_data = json.load(file)

    if hint:
        print(f"Hint: {vault_data['user']['hint']}")
        return
        
    pw = getpass.getpass("Enter your password: ")

    hashed_from_file = vault_data["user"]["user_pw"]
    salt_from_file = vault_data["user"]["salt"]

    combined = str(salt_from_file) + pw
    hashed = hashlib.sha256(combined.encode())

    unlocked_time = time.time()
    auto_lock = True

    if disable:
        auto_lock = False

    if hashed.hexdigest() == hashed_from_file:
        session = {
            "unlocked_time": unlocked_time,
            "autolock_enabled": auto_lock,
            "autolock_timeout": 120,
            "active": True
        }

        with open("session.json", "w") as f:
            json.dump(session, f, indent=4)

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
