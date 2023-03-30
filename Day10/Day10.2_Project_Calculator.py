def calculate(number1, operator_selected, number2):
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2
    return result
new_first_number = True
while new_first_number == True:
	sonuc = float(input("What's the first number?: "))
	while True:
		operator = input("+\n-\n*\n/\nPick an operation: ")
		secondnumber = float(input("What is the next number?: "))
		sonuc = calculate(number1=sonuc, operator_selected=operator, number2=secondnumber)
		game_continue = input(f"Result is {sonuc}. If you want to continue with this result type 'Continue'. If you want to continue with new number type 'New'\n").lower()
		if game_continue == "new":
			break
		elif game_continue == "continue":
			continue