import json
import time

def session_valid():
    with open("session.json", "r") as f:
        data = json.load(f)

    if data["active"] == False:
        print("Vault is locked")
        with open(".lock", "w") as f:
            f.write("locked")
        exit(1)
    
    if data["autolock_enabled"]:
        if time.time() - data["unlocked_time"] > data["autolock_timeout"]:
            data["active"] = False

            with open("session.json", "w") as f:
                json.dump(data, f, indent=4)
                print("Vault auto-locked")
            exit(1)