import random
import string

def generate_password(num_of_characters,password_strength):
    password =""
    if password_strength == "easy":
        password = ''.join(random.choices(string.digits,k=num_of_characters))
    elif password_strength == "medium":
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=num_of_characters))
    elif password_strength == "hard":
        password = ''.join(random.choices(string.ascii_letters+string.digits+string.punctuation, k=num_of_characters))
    return password



num_of_characters_input = int(input("Enter number of characters (must be bigger than 8): ")) 
password_strength_input = input("Enter a password strength - easy, medium, or hard: ")

if num_of_characters_input < 8:
    print("Password must be longer than 8 characters.")
elif password_strength_input not in ("easy", "medium", "hard"):
    print("Password strength must be one of the following: easy, medium, or hard.")
else:
    password = generate_password(num_of_characters_input,password_strength_input)
    print(f"The generated password is : {password}")    