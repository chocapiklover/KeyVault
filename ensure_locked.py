import os

def ensure_locked():
    if os.path.exists(".lock"):
        print("Vault is locked. Please unlock first.")
        return