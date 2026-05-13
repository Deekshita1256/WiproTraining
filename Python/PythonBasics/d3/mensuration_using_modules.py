#We are going to use the module we created that is circle.py
from mypackage.circle import areaofcircle as ac
from mypackage.circle import perimeterofcircle as pc


radius=int(input("Enter the radius: "))
print('Area: ',ac(radius))
print('Perimeter: ',pc(radius))