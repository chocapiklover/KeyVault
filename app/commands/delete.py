import json
from app.ensure_unlocked import ensure_unlocked
from cryptography.fernet import Fernet
from app.validate_pw import validate_pw
from app.session_valid import session_valid
from app.pw_generate import random_pw_generator

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
    answer = input("Are you sure you want to delete? (y/n)")
    if answer == "y":
        del vaultdata["vault"][match]

        with open("vault.json", "w") as f:
            json.dump(vaultdata, f, indent=4)

        print(f"✅ Successfully deleted '{service.upper()}' from your vault.")
    else:
        print(f"Cancelled delete")
        exit(1)
