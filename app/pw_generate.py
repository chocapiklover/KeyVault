import secrets
import string

def random_pw_generator(length=16):
    char_pool = string.ascii_letters + string.digits

    generated_pw = ''.join(secrets.choice(char_pool) for _ in range(length))

    return generated_pw