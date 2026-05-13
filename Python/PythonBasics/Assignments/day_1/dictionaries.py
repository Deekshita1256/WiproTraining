#Dictionary Operations

my_details={'Name': 'Durgam Deekshita',
            'Age': 23,
            'Hobby': 'Reading Books'}
print('My details are: ',my_details)

name = my_details['Name']
print('My name is: ',name)

my_details['Favourite_food'] = 'Biryani'

my_details['Hobby'] = 'Vibe coding'
print('The updated details are: ',my_details)

print('All the keys are: ',list(my_details.keys()))
print('The values of all the keys are: ',list(my_details.values()))

age = my_details.pop('Age')
print('The updated details after removing age key: ',my_details)
