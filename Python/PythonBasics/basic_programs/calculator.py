#Simple Calculator
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
sym=input("Enter the operation symbol \nExample: '+','-','*','/': ")
if sym=='+':
    print('sum: ',x+y)
elif sym=='-':
    print('subtraction: ',x-y)
elif sym=='/':
    print('division: ',x/y)
elif sym=='*':
    print('product: ',x*y)
elif sym=='//':
    print('modular division: ',x//y)
elif sym=='%':
    print('remainder: ',x%y)
elif sym=='^':
    print('Exponential value: ',x^y)
else:
    print("Enter the symbol again")