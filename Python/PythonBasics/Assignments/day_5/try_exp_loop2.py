while True:
    try:
        number = int(input("Enter a number: "))
        print(f"Your number is: {number}")
        break

    except ValueError:
        print("ERROR!! Invalid input. Please enter numeric value only. Try again.")