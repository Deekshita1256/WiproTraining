#tuple operations

cities = ('Tokyo','Paris','Seoul')
print('The cities i would like to visit are: ',cities)

first_city = cities[0]
last_city = cities[-1]
print('The first city in my list is: ',first_city)
print('The last city in my list is: ',last_city)

cities2 = ('London','Bangkok')
concated_cities = cities + cities2
print('The Concatenation of two tuples is: ',concated_cities)

cities[0] = 'Kyoto'
print('The list after changing the first city to Kyoto: ',cities[0])

(city1, city2, city3, city4, city5) = concated_cities
print('For variable "city1" the value is: ',city1)
print('For variable "city2" the value is: ',city2)
print('For variable "city3" the value is: ',city3)
print('For variable "city4" the value is: ',city4)
print('For variable "city5" the value is: ',city5)
