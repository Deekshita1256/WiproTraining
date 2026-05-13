import os

# Read and Write functions

def write_txt(filename):
    text = input("Enter some text to save into the file: ")
    with open(filename, "w" ) as file:
        file.write(text)
        print("Text is successfully written into the file")

def read_text(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)

# Driver code
filename = "output.txt"
write_txt(filename)
print("The content of the file are: ")
read_text(filename)
