height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

try:
    h = float(height)
except:
    print("Please enter a number")
    quit()

try:
    w = float(weight)
except:
    print("Please enter a number")
    quit()

bmi = w / (h * h)
print(int(bmi))
