import re
import getpass

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
            pw = getpass.getpass("🔸 Password (input hidden): ")
            validate_pw(pw)
        if option == "n":
            return False
            
    elif score == 3 or score == 4:
        print("aight kinda mid")
        option = input("you wanna change it y/n")
        if option == "y":
            pw = getpass.getpass("🔸 Password (input hidden): ")
            validate_pw(pw)
        if option == "n":
            return False

    return password