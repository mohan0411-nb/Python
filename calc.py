print("-----SIMPLE CALC-----")

num1 = float(input("enter the 1st number:"))
num2 = float(input("enter the 2nd number:"))

print("choose operation: + - * /")
op = input("Enter the operator:")

if op == "+":
    print("Result",num1 + num2)

elif op == "-":
    print("Result", num1 - num2)

elif op == "*":
    print("Result", num1 / num2)

else:
    print("Invalid number")






