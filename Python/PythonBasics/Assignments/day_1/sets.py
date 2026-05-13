#Set Operations

colours = {'Red','Blue','Green','Yellow','Purple'}
print('My set of colours are: ',colours)

colours.add('Orange')
colours.remove('Yellow')
print('The set after adding new colour and remove another colour: ',colours)

new_colours = {'Black','Maroon','Peach'}
print('The intersection of two sets is: ',colours.intersection(new_colours))
print('The union of two sets is: ',colours.union(new_colours))
print('The difference between two sets are: ',colours.difference(new_colours))

if 'Red' in colours:
    print('Yes!! Red is in the set')
else:
    print('No!! Red is not in the set')

fruits = ['orange','mango','cherry','orange','apple']
print('The list of fruits are: ',fruits)

new_fruits=set(fruits)
print('The set of fruits are: ',new_fruits)