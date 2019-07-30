num = input("Enter the first number: ")
num2 = input("Enter the second number: ")
op = input("Choose the operation (+, -, /, *): ")
if (num.isdigit() and num2.isdigit()) != True :
	print("Invalid numbers input.")
else:
	if op == "+":
		print("The answer is",int(num) + int(num2))
	elif op == "-":
		print("The answer is",int(num) - int(num2))
	elif op == "/":
		print("The answer is",int(num) / int(num2))
	elif op == "*":
		print("The answer is",int(num) * int(num2))
	else:
		print("Invalid operation input.")
	