# Here I am making a simple password generator I saw this idea from my friend's
# 100 DayOfCode challenge as I ran out of ideas
import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
             'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeric_character = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '_']

print("Password Generator!")
no_of_letters = int(input("Enter the number of letters that you want in your password: "))
no_of_numbers = int(input("Enter the number of numeric characters that you want in your password: "))
no_of_symbols = int(input("Enter the number of symbols that you want in your password: "))

password = []

for i in range(0, no_of_letters):
    password.append(random.choice(alphabets))

for i in range(0, no_of_numbers):
    password.append(random.choice(numeric_character))

for i in range(0, no_of_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)

print("Your password: ", end=" ")
for i in password:
    print(i, end="")
