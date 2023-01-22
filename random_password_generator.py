import string
import random

letters = list(string.ascii_letters)
numbers = list(string.digits)
characters = ["!","?","*","^","+","$","%","#",",","."]

number = int(input("How many digit password do you want?\n"))

print("Your password: ",end="")
for i in range(number):
    random_letters = random.choice(letters)
    random_numbers = random.choice(numbers)
    random_characters = random.choice(characters)

    rastgele_liste = [random_letters,random_numbers,random_characters]

    randomchoice = random.choice(rastgele_liste)
    for i in range(1):
        print(randomchoice,end="")