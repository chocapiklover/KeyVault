import os

def ensure_unlocked():
    if os.path.exists(".lock"):
        print("Vault is locked. Please unlock first.")
        exit(1)