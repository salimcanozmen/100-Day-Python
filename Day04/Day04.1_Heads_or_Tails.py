#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
#Write the rest of your code below this line 👇

randomint = random.randint(0, 1)
if randomint == 1:
    print("Heads")
elif randomint == 0:
    print("Tails")
