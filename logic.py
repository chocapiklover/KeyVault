import getpass
import os
import hashlib
import json
from ensure_unlocked import ensure_unlocked
from cryptography.fernet import Fernet
import base64
import pyperclip
from validate_pw import validate_pw
from session_valid import session_valid
import time


def init():
    if os.path.exists("vault.json"):
        print("you already have a vault pls use unlock")
        exit(1)

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
    session_valid()
    print("\n🔐 Let's add a new service to your vault\n")

    service = input("🔹 Service name (e.g., GitHub, Gmail): ").strip()
    
    with open("vault.json", "r") as f:
        data = json.load(f)
    
    if service in data["vault"]:
        print("this service already exists")
        exit(1)

    username = input("🔹 Username / Email: ").strip()
    pw = getpass.getpass("🔸 Password (input hidden): ")

    new_pw = validate_pw(pw)

    print("\n📂 Opening your vault...\n")

    key = Fernet.generate_key()
    formatted_key = base64.b64encode(key).decode() 
   
    f = Fernet(key)

    if new_pw == False:
        token = f.encrypt(pw.encode())
    else:
        token = f.encrypt(new_pw.encode())
    formatted_token = base64.b64encode(token).decode() 

    data["vault"][service] = {
        "username": username,
        "token": formatted_token,
        "key": formatted_key
    }

    with open("vault.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"\n✅ Successfully added '{service.upper()}' to your vault.\n")
    print("🔒 Reminder: Run `lock` to secure your vault when you're done.\n")



def unlock():
    if not os.path.exists(".lock"):
        print("already unlocked!")
        exit(1)
    pw = getpass.getpass("Enter your pw: ")

    with open("vault.json", "r") as file:
        vault_data = json.load(file)

    hashed_from_file = vault_data["user"]["user_pw"]
    salt_from_file = vault_data["user"]["salt"]

    combined = str(salt_from_file) + pw
    hashed = hashlib.sha256(combined.encode())

    unlocked_time = time.time()
    auto_lock = True
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


def lock():
    if os.path.exists(".lock"):
        print("Vault is already locked.")
    else:
        with open(".lock", "w") as f:
            f.write("locked")
        print("🔒 Vault is now locked.")


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

def get(service):
    ensure_unlocked()
    session_valid()

    print(f"\n🔐 Retrieving credentials for service: **{service}** ...")

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
    copy_to_clipboard = input("Type 'y' to copy the password to clipboard").strip().lower()


    if copy_to_clipboard == "y":
        pyperclip.copy(decoded_pw)


def delete(service):
    ensure_unlocked()
    session_valid()
    print(f"\n🔐 Searching for: **{service}** ...")

    with open("vault.json", "r") as f:
        vaultdata = json.load(f)
        vault_services = vaultdata["vault"]
    
    match = None

    for services in vault_services:
        if services.lower() == service.lower():
            match = services
            break

    if not match:
        print(f"❌ No entry found for '{service}'.")
        return

    del vaultdata["vault"][match]

    with open("vault.json", "w") as f:
        json.dump(vaultdata, f, indent=4)

    print(f"✅ Successfully deleted '{service.upper()}' from your vault.")

def update(service):
    ensure_unlocked()
    session_valid()

    option = input("What do you want to update? 1) Username 2) Password: ").strip()

    with open("vault.json", "r") as f: #getting json
        data = json.load(f)

    match = None

    for vault_service in data["vault"]:
        if vault_service.lower() == service.lower():
            match = vault_service
            break

    if not match:
        print(f"❌ No entry found for '{service}'.")
        exit(1)

    service_data = data["vault"][match]

    if option == "1":
        new_username = input("Enter new username: ").strip()
        service_data["username"] = new_username
        with open("vault.json", "w") as f:
            json.dump(data, f, indent=4)

        print("✅ Username updated successfully.")
    elif option == "2":
        if input("Are you sure you want to update the password? (y/n): ").strip().lower() == "y":
            new_password = getpass.getpass("Enter new password: ")
            confirm_pw = getpass.getpass("Confirm new password: ")

            if new_password != confirm_pw:
                print("❌ Passwords do not match. Update cancelled.")
                exit(1)
            
            key = Fernet.generate_key()
            formatted_key = base64.b64encode(key).decode() 
        
            f = Fernet(key)

            token = f.encrypt(new_password.encode())
            formatted_token = base64.b64encode(token).decode() 

            data["vault"][service] = {
                "username": data["vault"][match]['username'],
                "token": formatted_token,
                "key": formatted_key
                
            }

            with open("vault.json", "w") as f:
                json.dump(data, f, indent=4)
            print("✅ Password updated successfully.")
            

