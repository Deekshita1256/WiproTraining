# Try and Except

user_string = input("Enter a string: ")

try:
    number = int(user_string)
    print(f"Successfully converted string to number. Your number is: {number}")
except ValueError:
    print("Error!! The string does not complete numeric values")
