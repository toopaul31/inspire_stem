# this is a program used to give the volume of a sphere and cylinder
# date : 21/02/2024
# name : paul too
import math

r = float(input("radius of the cylinder :"))
h = float(input("height of the cylinder :"))

v = (4/3)*(math.pi)*r**3

print("the volume of a sphere :")

r2 = float(input("enter the radius :"))
h = float(input("enter the height :"))

v2 = (math.pi)*r**2*h

print("the volume of cylinder :",v2)