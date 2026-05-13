# Try and except with Lists

try:
    lst = list(map(int,input("Enter numbers with spaces: ").split()))
    idx = int(input("Enter a index value number: "))

    print(f"The element at index {idx} is: {lst[idx]}")

except IndexError:
    print("Error!! Enter the correct index value")