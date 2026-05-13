import os

with open("sources.txt", "r") as file:
    content = file.read()
    print("The content is read successfully")

with open("destination.txt", "w") as file:
    file.write(content) # If the file does not exist then it will create the file
    print("The content is successfully copied into this file")
