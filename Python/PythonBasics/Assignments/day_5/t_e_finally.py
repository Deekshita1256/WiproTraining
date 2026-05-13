from logging import exception

filename = input("Enter the filename to read: ")

try:
    file = open(filename, "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print(f"ERROR!! {filename} was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("The Execution completed: File operation attempt finished.")