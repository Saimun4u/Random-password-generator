import string
import random

characters = string.ascii_letters + string.digits + "!@#$%^&*()"

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    
    #Shuffle characters for the password to be generated
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))
    
    # Shuffle the password generated
    random.shuffle(password)
