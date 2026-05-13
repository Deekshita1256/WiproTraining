from openpyxl import Workbook, load_workbook
import os

def write_excel(filename):
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["Name", "Age"])
    sheet.append(["Riya Gupta", 25])
    sheet.append(["Ankit Das", 27])
    workbook.save(filename)
    print("Data is successfully updated")

def read_excel(filename):
    workbook = load_workbook(filename)
    sheet = workbook.active
    for row in sheet.iter_rows(values_only = True):
        print(f"Name: {row[0]}, Age: {row[1]}")

def delete_excel(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} does not exists")

filename = "myexcel.xlsx"
write_excel(filename)
print("Data is read from Excel file: ")
read_excel(filename)
delete_excel(filename)