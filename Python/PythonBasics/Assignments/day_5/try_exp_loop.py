while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        res = num1/num2

        print(f"Division result is: {res}")
        break

    except ValueError:
        print("Invalid input!! Please enter number only.")

    except ZeroDivisionError:
        print("Error! Cannot divide with zero. Try again.")