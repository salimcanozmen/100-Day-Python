import random
import os
clear = lambda: os.system("cls")
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def atama(char):
    if char == "A":
        return 11
    elif char == "J":
        return 10
    elif char == "Q":
        return 10
    elif char == "K":
        return 10
    else:
        return char
def atama2(char):
    if char == "A":
        if sum(complist) + 11 > 21:
            return 1
        else:
            return 11
    elif char == "J":
        return 10
    elif char == "Q":
        return 10
    elif char == "K":
        return 10
    else:
        return char
def is_game_over():
    if sum(complist) > sum(humanlist):
        return "2"
    while sum(complist) < 17:
        compnew = random.choice(cards)
        compnewval = atama2(compnew)
        complist.append(compnewval)
    if sum(complist) > 21:
        return "1"
    elif sum(complist) > 16 and sum(complist) > sum(humanlist):
        return "2"
def blackjack():
    human1 = random.choice(cards)
    human2 = random.choice(cards)
    comp1 = random.choice(cards)
    human1val = atama(human1)
    humanlist.append(human1val)
    human2val = atama2(human2)
    humanlist.append(human2val)
    comp1val = atama(comp1)
    complist.append(comp1val)
    if sum(humanlist) == 21:
        comp2 = random.choice(cards)
        comp2val = atama(comp2)
        complist.append(comp2val)
        if sum(complist) != 21:
            return "1"
        else:
            return "0"
    print(f"Your cards are {human1} and {human2}, current score: {sum(humanlist)}\nComputer's first card: {comp1}")
    while True:
        newround = input("Type 'Hit' for another card. Type 'Pass' to pass: ").lower()
        if newround == "hit":
            humannew = random.choice(cards)
            humannewval = atama2(humannew)
            humanlist.append(humannewval)
            if sum(humanlist) > 21 and 11 not in humanlist:
                return "2"
            elif sum(humanlist) > 21 and 11 in humanlist:
                humanlist.remove(11)
                humanlist.append(1)
            elif humanlist == 21:
                while True:
                    while complist < 17:
                        compnew = random.choice(cards)
                        compnewval = atama2(compnew)
                        complist.append(compnewval)
                    if sum(complist) == 21:
                        return "3"
                    elif sum(complist) > 21:
                        return "1"
            if sum(humanlist) < 21:
                print(f"You picked {humannew}. Your cards are {humanlist} with a total score of: {sum(humanlist)}\n")
                continue  
        elif newround == "pass":
            comp2 = random.choice(cards)
            comp2val = atama2(comp2)
            complist.append(comp2val)
            x = is_game_over()
            return x   
print(logo)
cards = ["A", 2 , 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
while True:
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == "n":
        quit()
    elif play_game =="y":
        humanlist = []
        complist = []
        clear()
        print(logo)
        winner = blackjack()
        if winner == "1":
            winner = "You Win!"
        elif winner == "2":
            winner = "You Lost!"
        elif winner == "0":
            winner = "Draw!"
        elif winner == "3":
            winner == "You win with Blackjack!"
        print(f"Your final cards are: {humanlist} with a total score of: {sum(humanlist)}\nComputer's final cards are: {complist} with a total score of: {sum(complist)}\n{winner}")