import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
numOfLetters = int(input("How many letters would you like in your password? \n"))
numOfSymbols = int(input("How many symbols would you like? \n"))
numOfDigits = int(input("How many digits would you like?\n"))

password  = ""

for i in range(numOfLetters):
    password += random.choice(letters)

for i in range(numOfDigits):
    password += random.choice(numbers)

for i in range(numOfSymbols):
    password += random.choice(symbols)

password = ''.join(random.sample(password, len(password)))

print(f"Here is your password: {password}")
