import os

# Functions to append and read

def append_text(filename, content):
    with open(filename, "a") as file:
        file.write(content)
        print("The content is successfully appended")

def read_text(filename):
    with open(filename, "r") as file:
        context = file.read()
        print(context)

# Driver code
if __name__ == "__main__":
    filename = "log.txt"

    content = '\nThe order for 5 Laptops and 3 Desktops is received'
    append_text(filename, content)
    print(f"After appending the file content is:")
    read_text(filename)