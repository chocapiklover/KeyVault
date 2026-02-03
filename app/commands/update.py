import getpass
import json
from app.ensure_unlocked import ensure_unlocked
from cryptography.fernet import Fernet
import base64
from app.validate_pw import validate_pw
from app.session_valid import session_valid
from app.pw_generate import random_pw_generator

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
            

