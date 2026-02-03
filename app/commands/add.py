import getpass
import json
from app.ensure_unlocked import ensure_unlocked
from cryptography.fernet import Fernet
import base64
from app.validate_pw import validate_pw
from app.session_valid import session_valid
from app.pw_generate import random_pw_generator





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
