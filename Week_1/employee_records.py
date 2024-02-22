# this program is used to show the employee records
# date : 21/02/2024
# name : paul too
# employee records

n = input("name :")
a = input("age :")
s = float(input("salary :"))
b = float(input("bonus :"))

t = s + b


print("employee records :",n)
print("age :",a)
print("salary :",s)
print("bonuses :",b)
print("total income :",t)

s2 = (130/100 * s)
t2 = s2 + b
print("employee's new bonus :",b)
print("employee's final total income :",t2)