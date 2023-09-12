import string
import random

p1 = string.ascii_letters
p2 = string.digits
p3 = string.punctuation

char = int(input("How many letters put in the password: "))
number = int(input("How many numbers to be included: "))
special = int(input("How many special characters should be used: "))

password = []

for i in range (0, char):
    char_pass = random.choice(p1)
    password.append(char_pass)

for i in range (0, number):
    num_pass = random.choice(p2)
    password.append(num_pass)

for i in range (0, special):
    special_pass = random.choice(p3)
    password.append(special_pass)

random.shuffle(password)
print("Your password is ready: ",''.join(password))