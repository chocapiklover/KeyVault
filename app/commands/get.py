import json
from app.ensure_unlocked import ensure_unlocked
from cryptography.fernet import Fernet
import base64
import pyperclip
from app.validate_pw import validate_pw
from app.session_valid import session_valid
from app.pw_generate import random_pw_generator





def get(service, copy=False):
    ensure_unlocked()
    session_valid()

    print(f"\n🔐 Retrieving credentials for service: **{service}** ...\n")

    with open("vault.json", "r") as f:
        data = json.load(f)

    service_data = data["vault"].get(service)
    
    if not service_data:
        print(f"❌ No entry found for '{service}'.")
        return

    username = service_data["username"]
    token = base64.b64decode(service_data["token"]) 
    key =  base64.b64decode(service_data["key"]) 

    f = Fernet(key)
    byte_pw = f.decrypt(token) 
    decoded_pw = byte_pw.decode()

    print("\n✅ Credentials successfully retrieved:\n")
    print(f"   🧑 Username: {username}")
    print(f"   🔑 Password: {decoded_pw}\n")
    print("📋 You can now use your credentials. Stay safe!\n")
    print("🔒 Reminder: Run `lock` to secure your vault when you're done.\n")
    
    if not copy:
        copy_to_clipboard = input("Type 'y' to copy the password to clipboard: ").strip().lower()
        if copy_to_clipboard == "y":
            pyperclip.copy(decoded_pw)
            print("🔑 Password copied to clipboard.")
            return

