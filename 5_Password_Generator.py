#day 5 - password generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
diffChoice = input("would you like easy mode or hard mode??\n")

if(diffChoice == "yes"):

    password = ""
    for letter in range(0, nr_letters):
        password = password + letters[random.randint(0, len(letters) - 1)]
    for symbol in range(0, nr_symbols):
        password = password + symbols[random.randint(0, len(symbols) - 1)]
    for number in range(0, nr_numbers):
        password = password + numbers[random.randint(0, len(numbers) - 1)]

    

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#SHE JUST RANDOMIZED THE PASSWORD AFTER IT WAS GENERATED, IT'S GENIUS
else:
    lengthOfPass = nr_letters + nr_symbols + nr_numbers
    numberOfTypesAvailable = 3

    password_list = []
    for letter in range(0, nr_letters):
        password_list += letters[random.randint(0, len(letters) - 1)]
    for symbol in range(0, nr_symbols):
        password_list += symbols[random.randint(0, len(symbols) - 1)]
    for number in range(0, nr_numbers):
        password_list += numbers[random.randint(0, len(numbers) - 1)]
    
    random.shuffle(password_list)

    for char in password_list:
        password += char
        
print(f"Password generated: {password}")