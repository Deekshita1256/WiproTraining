#List Operations

fruits = ['apple','banana','orange','pineapple','mango']
print('The list of fruits are: ',fruits)

fruits.extend(['watermelon','cherry'])
print('The list after adding two fruits: ',fruits)

fruits.remove('banana')
print('The list after removing one fruit: ',fruits)

second_fruit = fruits[1]
fourth_fruit = fruits[3]
print('The second fruit in the list is: ',second_fruit)
print('The fourth fruit in the list is: ',fourth_fruit)

sub_fruits = fruits[0:3]
print('The first three fruits are: ',sub_fruits)

length = len(fruits)
print('The length of the list is: ',length)
