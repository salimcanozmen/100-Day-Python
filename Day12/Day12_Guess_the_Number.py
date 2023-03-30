from art import guess_the_number_logo
import random
answer = random.randint(1, 100)
game_over = False
def choice(guess_number):
    global user_lives
    if guess_number == answer:
        print(f"You got it. The answer was {answer}")
        quit()
    elif guess_number > answer:
        user_lives -= 1
        print("Too high")
    elif guess_number < answer:
        user_lives -= 1
        print("Too low.")
while not game_over:
    user_lives = 0
    print(guess_the_number_logo)
    difficulty = input(f"Welcome to the Number Guessing Game\nI'm thinking a number between 1 and 100.\nTip; answer is {answer}\nChoose a difficulty. Type 'Easy' or 'Hard': ").lower()
    if difficulty == "easy":
        user_lives = 10
    elif difficulty == "hard":
        user_lives = 5
    while user_lives > 0:
        print(f"You have {user_lives} attemps remaining to guess the number\n")
        try:
            guess = int(input("Make a guess: "))
        except:
            print("Please enter a number")
        choice(guess)
        if user_lives > 0:
            print("Guess again.")
    print("You've run out of guesses you lose!")
    game_over = True
        