import random
import string

characters = string.ascii_letters + string.digits

length = int(input("How long should your password be? "))

password = ""

for i in range(length):
    password += random.choice(characters)

password_list = list(password)
random.shuffle(password_list)
password = "".join(password_list)

print("Your random password is:", password)