# this is a program to solve quadratic equation
# date :20/02/2024
# name : paul too
import math

a = float(input("Enter the coefficient of first term : "))
b = float(input("Enter the coefficient of second term : "))
c = float(input("Enter the constant : " ))

d = (float(b)**2) - 4 * (float(a)) * (float(c))

x_1 = ((-b + math.sqrt(d))/2 * a)
x_2 = ((-b + math.sqrt(d))/2 * a)

print("The solution of the quadratic equation :",x_1)
print("The solution of the quadratic equation :",x_2)
