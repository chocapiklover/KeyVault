import re
import getpass

import pyperclip
from app.pw_generate import random_pw_generator

def contains_uppercase(pw):
    for char in pw:
        if char.isupper():
            return True
    return False

def contains_lowercase(pw):
    for char in pw:
        if char.islower():
            return True
    return False

def contains_digit(pw):
    for char in pw:
        if char.isdigit():
            return True
    return False

def contains_special(pw):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if regex.search(pw):
        return True
    return False
        
def validate_pw(password):
    score = 0

    if len(password) >= 12: score += 1

    if contains_uppercase(password): score += 1
    if contains_lowercase(password): score += 1
    if contains_digit(password): score += 1
    if contains_special(password): score += 1
    #if is_common_password(pw): score -= 2
    
    if score <= 2:
        print("pw kinda weak go change now")
        option = input("you wanna change it y/n")

        if option == "y":
            choice = input("Do you want a securely generated password? (y/n): ").strip().lower()
            if choice == "y":
                print("🔸 Generating a secure password...")
                new_password = random_pw_generator()
                print(f"🔸 Generated Password: {new_password}")
                confirm = input("Do you want to use this password? (y/n): ").strip().lower()
                if confirm == "y":
                    print("🔸 Password accepted.")
                    copy_clipboard = input("Do you want to copy this password to clipboard? (y/n): ").strip().lower()
                    if copy_clipboard == "y":
                        pyperclip.copy(new_password)
                        print("🔑 Password copied to clipboard.")
                    return new_password
                else:
                    new_entered_pw = getpass.getpass("🔸 Password (input hidden): ")
                    return validate_pw(new_entered_pw)

            else:
                pw = getpass.getpass("🔸 Password (input hidden): ")
                return validate_pw(pw)
        if option == "n":
            return False
            
    elif score == 3 or score == 4:
        print("aight kinda mid")
        option = input("you wanna change it y/n")

        if option == "y":
            generated_secure_pw = input("Generate a secure password? (y/n): ").strip().lower()
            if generated_secure_pw == "y":
                print("🔸 Generating a secure password...")
                new_password = random_pw_generator()
                print(f"🔸 Generated Password: {new_password}") 
                confirm = input("Do you want to use this password? (y/n): ").strip().lower()
                if confirm == "y":
                    print("🔸 Password accepted.")
                    copy_clipboard = input("Do you want to copy this password to clipboard? (y/n): ").strip().lower()
                    if copy_clipboard == "y":
                        pyperclip.copy(new_password)
                        print("🔑 Password copied to clipboard.")
                    return new_password
                else:
                    new_entered_pw = getpass.getpass("🔸 Password (input hidden): ")
                    return validate_pw(new_entered_pw)
            else:
                pw = getpass.getpass("🔸 Password (input hidden): ")
                return validate_pw(pw)
    else:
        print("✅ Password is strong enough.")
        return password