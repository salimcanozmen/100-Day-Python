from higher_lower_data import data
from art import vs
from art import logo
import random
import os
clear = lambda: os.system("clear")

def display():
    choice_index = random.randint(0, len(data) - 1)
    return data.pop(choice_index)

# def compare(user_selection):
#     global display_a
#     global display_b
#     global score
#     if user_selection == "a":
#         if display_a["follower_count"] > display_b["follower_count"]:
#             clear()
#             print(logo)
#             score += 1
#             print(f"You're right! Your current score : {score}")
#             display_a = display_b
#             display_b = display()
#             return True
#         else:
#             clear()
#             print(logo)
#             print(f"Sorry, that's wrong. Final score: {score}")
#             return False
            
#     elif user_selection == "b":
#         if display_a["follower_count"] < display_b["follower_count"]:
#             clear()
#             print(logo)
#             score += 1
#             print(f"You're right! Your current score : {score}")
#             display_a = display_b
#             display_b = display()
#             return True
#         else:
#             clear()
#             print(logo)
#             print(f"Sorry, that's wrong. Final score: {score}") 
#             return False  
def compare(user_selection):
    global display_a
    global display_b
    global score
    if display_a["follower_count"] > display_b["follower_count"] and user_selection == "a":
        clear()
        print(logo)
        score += 1
        print(f"You're right! Your current score : {score}")
        display_a = display_b
        display_b = display()
        return True          
    elif display_a["follower_count"] < display_b["follower_count"] and user_selection == "b":
        clear()
        print(logo)
        score += 1
        print(f"You're right! Your current score : {score}")
        display_a = display_b
        display_b = display()
        return True
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}") 
        return False  
    
score = 0
display_a = display()
display_b = display()
print(logo)
game_continue = True
while game_continue:
    print(f"Compare A: {display_a['name']}, a {display_a['description']}, from {display_a['country']}\n{vs}\nAgainst B: {display_b['name']}, a {display_b['description']}, from {display_b['country']}\n")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    game_continue = compare(answer)

    