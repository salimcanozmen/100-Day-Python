# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

numt = int(name1.count("t")) + int(name2.count("t"))
numr = int(name1.count("r")) + int(name2.count("r"))
numu = int(name1.count("u")) + int(name2.count("u"))
nume = int(name1.count("e")) + int(name2.count("e"))
numl = int(name1.count("l")) + int(name2.count("l"))
numo = int(name1.count("o")) + int(name2.count("o"))
numv = int(name1.count("v")) + int(name2.count("v"))


digit1 = str(numt + numr + numu + nume)
digit2 = str(numl + numo + numv + nume)

love = int(digit1 + digit2)

if love < 10 or love > 90:
    print(f"Your score is {love}, you go together like coke and mentos")
elif love < 50 and love > 40:
    print(f"Your score is {love}, you are alright together.")
else:
    print(f"Your score is {love}.")

