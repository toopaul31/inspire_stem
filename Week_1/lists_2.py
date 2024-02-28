




friends = ("paul","manu","maryjane","mustafa","odhis","phyliss")

for friend in friends :
    print(friend)

enemies = friends[:] # copy one list into another
for enemies in enemies:
    print(enemies)

fruits = ("guava","lemon","orange","mango","passion","avocado")

# slice the list to get  part of the list

print(fruits[0:3])

del fruits[0]

print(fruits)

squares = [] # initializes an empty list

for x in range (0,11):
    squares.append(x**2)
print(squares)
    
