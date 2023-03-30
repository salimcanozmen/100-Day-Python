# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

x = ""
for letter in letters:
    if len(x) == nr_letters:
        break
    a = random.choice(letters)
    x += a

y = ""
for number in numbers:
    if len(y) == nr_numbers:
        break
    b = random.choice(numbers)
    y += b

z = ""
for symbol in symbols:
    if len(z) == nr_symbols:
        break
    c = random.choice(symbols)
    z += c
g = list(str(x) +str(y) + str(z))
random.shuffle(g)
sonuc= ""
for i in g:
    sonuc += i
print(sonuc)