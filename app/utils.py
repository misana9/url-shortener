import random
import string
from pwdlib import PasswordHash

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

password_hash = PasswordHash.recommended()

def hash_password(plain:str):
    return password_hash.hash(plain)


def verify_password(plain:str,hashed:str):
    return password_hash.verify(plain,hashed)

