import re

# txt = input("enter a text: ")
# bpat = input("Enter beginning pattern: ")
# epat = input("Enter ending pattern: ")
#
# bpat = "^" + bpat
# epat = epat + "$"
#
# match = re.search(pattern = bpat, string = txt)
# match1 = re.search(pattern = epat, string = txt)
#
# if match:
#     print("Beginning pattern available")
# else:
#     print("Beginning pattern not available")
#
# if match1:
#     print("Ending pattern available")
# else:
#     print("Ending pattern not available")

#Digits

# mbno = input("Enter the mobile number: ")
# #pat = '[0-9]' #This will not detect the whitespace. it is not perfect match
# pat = r"\d"
# #pat = r'[0-9]'
#
# if re.fullmatch(pattern = pat, string = mbno):
#     print("Only digits are present")
# else:
#     print("Other characters are all present")


#Usernam

# un = input("Enter UN: ")
# #pat = r"[a-z]{8}"
# #pat = r"^[a-z]{8}$" #This will match if it is exactly 8 characters
# #pat = r"^[a-z_]{8}$" #It will allow _
# pat = r"^[a-z_]{8,}$" # This will tell min 8 character max infinite
#
# if re.match(pattern = pat, string = un): #match will only match first 8 characters only
#     print('Valid')
# else:
#     print("Invalid")

# Email

# emailid = input("Enter your emailid: ")
# pat = r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"
#
# if re.match(pattern = pat, string = emailid): #match will only match first 8 characters only
#     print('Valid')
# else:
#     print("Invalid")

#Password

# pwd = input("Enter the password: ")
# pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[_+=@]).{8,}$"
#
# if re.match(pattern = pat, string = pwd): #match will only match first 8 characters only
#     print('Valid')
# else:
#     print("Invalid")


txt = input("Enter text: ")
pat = r"\s+"

#print(re.sub(pattern = pat, string = txt, repl = ' '))

print(re.split(pattern = pat, string = txt))