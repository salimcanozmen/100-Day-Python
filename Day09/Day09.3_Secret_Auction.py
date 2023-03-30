logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
import os
clear = lambda: os.system("clear")
contain = {}
def x(bidder_name, bidder_bid):
    contain[bidder_name] = bidder_bid
while True:
    name = input("Welcome to the secret auction program.\nWhat is your name?: ")
    bid = int(input("What is your bid?: $"))
    x(name, bid)   
    other_bidders = input("Are they any other bidders? Type 'Yes or 'No'. ").lower()
    if other_bidders == "no":
        break
    if other_bidders == "yes":
        clear()
        print(logo)
winner = None
for i in contain:
    if winner == None:
        winner = contain[i]
    elif contain[i] > winner:
        winner = i
print(f"The winner is {winner} with a bid of ${contain[winner]}") 
    