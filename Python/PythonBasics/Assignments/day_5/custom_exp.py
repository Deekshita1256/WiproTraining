class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!!")
    print(f"You entered: {num}")

except NegativeNumberError as e:
    print(f"Custom Error: {e}")

except ValueError:
    print("Error!! Please enter a valid number.")