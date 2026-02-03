import os
from app.ensure_unlocked import ensure_unlocked
from cryptography.fernet import Fernet
from app.validate_pw import validate_pw
from app.session_valid import session_valid
from app.pw_generate import random_pw_generator

def lock():
    if os.path.exists(".lock"):
        print("Vault is already locked.")
    else:
        with open(".lock", "w") as f:
            f.write("locked")
        print("🔒 Vault is now locked.")
