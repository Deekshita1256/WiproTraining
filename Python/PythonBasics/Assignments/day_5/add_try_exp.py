def add_numbers(a, b):
    try:
        result = a + b
        print(f"The sum of {a} and {b} is: {result}")

    except TypeError:
        print("ERROR!! Both arguments must be numbers.")

# Driver code

if __name__ == "__main__":
    print("Test 1 (Valid): ")
    add_numbers(10,15)

    print("Test 2 (Invalid): ")
    add_numbers(9,'five')
