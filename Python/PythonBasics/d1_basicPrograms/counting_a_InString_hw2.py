#Counting the letter 'a' in the input string and print the count
str=input("Enter a string: ")
count=0
id=0
for id,i in enumerate(str):
    if i=='a':
        count=count+1
print(count)