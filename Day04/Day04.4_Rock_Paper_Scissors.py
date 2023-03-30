rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
while True:
    import random
    secim = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
    if secim == "0":
        print(rock)
    elif secim == "1":
        print(paper)
    elif secim == "2":
        print(scissors)
    elif secim == "done":
        quit()
    # tas = "0"
    # kagit = "1"
    # makas = "2"
    # x = [tas, kagit, makas]
    pc = random.randint(0, 2)

    if pc == 0:
        if secim == "0":
            print(f"Computer chose:\n{rock}\nDraw!")
        elif secim == "1":
            print(f"{rock}\nYou win!")
        elif secim == "2":
            print(f"{rock} \nYou lose!")
    if pc == 1:
        if secim == "0":
            print(f"{paper}\nYou lose!")
        elif secim == "1":
            print(f"{paper}\nDraw!")
        elif secim == "2":
            print(f"{paper}\nYou win!")
    if pc == 2:
        if secim == "0":
            print(f"{scissors}\nYou win!")
        elif secim == "1":
            print(f"{scissors}\nYou lose!")
        elif secim == "2":
            print(f"{scissors}\nDraw!")
    continue
