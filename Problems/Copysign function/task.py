import math

# place `import` statement at top of the program


# don't modify this code or the variables may not be available
x, y = map(float, input().split(' '))
print(math.copysign(x, y))
