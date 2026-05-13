# ZeroDivisionError and ValueError
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    div = num1/num2
    print(f"The division of {num1} and {num2} is: {div}")

except ZeroDivisionError:
    print("Error!! Cannot divide number with zero")

except ValueError:
    print("Error!! Please enter a valid number(non-string)")

