# strings in python
# date :22/02/2024
# name : paul too

city = "nairobi"

print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])
print(city[-1])
print(city[-2]) #

# convert to the uppercase


print(city)
print("\n") # print a new line
print(city.upper())

name = "PAUL TOO"
print(name)
print(name.lower()) # converts string to lower case

town = "    Naivasha    "

print(town)
print("\t") # new tab
print(town.strip())


f_name = "paul"
s_name = "too"

full_name = f_name + s_name

print(full_name)


# replacing a character

fruit = "OrangeOOOO"

print(fruit.replace("O","Y"))

subject = "physical,sciences"

print(subject.split(":"))

age = 19
height = 5.8

print("I am {0} years old and {1} meters tall " .format(age,height))

activity = "dancing"
print("my hobby is %s" %(activity))

# printing a float
height = 1.233349
print("my height is %5.3f"% (height))

# printing an integer

age = 23 
print("my age is %d " %(age))

name = "paul too"
print(len(name))

print(f"my full name is {name}")

school = "Engineering"
course = "Electrical"

print(" i am studying {course} in the school of {school}" .format(course = "medicine",school = "human science"))