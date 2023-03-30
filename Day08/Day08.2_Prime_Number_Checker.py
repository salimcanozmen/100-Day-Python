#Write your code below this line 👇
def prime_checker(number):
    asal = []
    for i in range(1, number + 1):
        x = str(i)
        asal.append(x)
        if number % i != 0:
            if (number / i) % int(number / i) != 0:
                asal.remove(x)
    count = 0
    for i in asal:
        count += 1
    if count > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")                      
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
