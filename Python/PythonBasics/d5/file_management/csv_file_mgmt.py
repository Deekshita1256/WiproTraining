import csv
import os

def write_csv(filename):
    data = [
        {"name": "Deekshita", "age": 23},
        {"name": "Ankit", "age": 25}
    ]

    columnames = ["name", "age"]
    with open(filename, "w", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames = columnames)
        writer.writeheader()
        writer.writerows(data)
        print("The data is updated")

def read_csv(filename):
    with open(filename, "r", newline = "\n") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"name: {row['name']}, Age: {row['age']}")

def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} does not exists")


filename = "myfile.csv"
write_csv(filename)
print("Data is read from the file")
read_csv(filename)
delete_csv(filename)

