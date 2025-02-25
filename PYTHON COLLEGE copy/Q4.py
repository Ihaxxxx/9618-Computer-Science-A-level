import random

NumberArray = [ [random.randint(1,101),random.randint(1,101)] for index in range(10)]

# print(NumberArray)

ArrayLenght = len(NumberArray)-1
for x in range(0,ArrayLenght-1):
 for y in range(0,ArrayLenght-2):
    for z in range(0,ArrayLenght-y-2):
        if NumberArray[x][z] > NumberArray[x][z+1]:
          TempValue = NumberArray[x][z]
          NumberArray[x][z] = NumberArray[x][z+1]
          NumberArray[x][z+1] = TempValue

# print(NumberArray)
