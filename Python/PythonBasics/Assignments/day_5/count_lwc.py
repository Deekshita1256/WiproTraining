import os

# Reading the file

with open("sample.txt", 'r') as file:
    lines = file.readlines()

    count_lines = len(lines)
    count_words = sum(len(line.split()) for line in lines)
    count_char = sum(len(line) for line in lines)

print(f"Number lines: {count_lines}")
print(f"Number of words: {count_words}")
print(f"Number of characters: {count_char}")


