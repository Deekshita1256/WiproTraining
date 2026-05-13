#Understanding functions and drivers
# #Fist way of func
# def addition(n1,n2):
#     sum1 = n1+n2
#     return sum1
# #Driver code
# num1=int(input("Enter your first number: "))
# num2=int(input("Enter your second number: "))
#
# res=addition(num1, num2)
# print('Add: ',res)

#Second Way
def addition(n1,n2):
    return n1+n2

def subtraction(n1,n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))

res1=addition(num1, num2)
res2=subtraction(n2=num1,n1=num2)
res3=multiplication(num1, num2)
res4=div(num1, num2)

print('Add: ',res1)
print('Sub: ',res2)
print("Mul: ",res3)
print("Div: ",res4)