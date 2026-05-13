import os

filename = input("Enter a filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(f"The content of the file are: {content}")

except FileNotFoundError:
    print(f"Error!! The {filename} file is NOT FOUND ")

