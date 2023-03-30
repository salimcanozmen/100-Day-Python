#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to Tip Calculator")
bill = input("What was the total bill? $")
fbill = float(bill)
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
ftip = float(tip)
people = input("How many people to split the bill? ")
ipeople = int(people)
newtip = (ftip / 100) + 1.00
final = (fbill / ipeople * newtip)
#a = (round(final, 2))
a = "{:.2f}".format(final)
print(a)
#print(f"Each person should pay {a:.2f}")
