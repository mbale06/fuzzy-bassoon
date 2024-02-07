import random

# Create how long the list is gonna be (i set to 5 and 20 so its not gonna be too short or too long)
a = random.randrange(5, 15)
b = random.randrange(5, 15)

# Using range to create list based with a random length but still in ascending order
range_a = range(1, a)
range_b = range(1, b)

# Making list with a random number order and random length (also sorted)
x = sorted(random.choices(range_a, k = a))
y = sorted(random.choices(range_b, k = b))

# Display the individual list
print(x)
print(y)

# The same number from two list before
xy = list(set(x).intersection(set(y)))
print(xy)




