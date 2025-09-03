import random

ArrayLength = 10
NumberArray = [[random.randint(1, 3) for _ in range(ArrayLength)] for _ in range(ArrayLength)]


for x in range(0,ArrayLength-1):
 for y in range(0,ArrayLength-2):
    for z in range(0,ArrayLength-y-2):
        
        if NumberArray[x][z] > NumberArray[x][z+1]:
          TempValue = NumberArray[x][z]
          NumberArray[x][z] = NumberArray[x][z+1]
          NumberArray[x][z+1] = TempValue

print(NumberArray)



for i in range(ArrayLength):
 x = ""
 for j in range(ArrayLength):
   x += str(NumberArray[i][j]) + " "
 print(x)  

def BinarySearch(SearchArray,Lower,Upper,SearchValue):
  if Upper >= Lower:
    mid = (Lower + (Upper-1)) // 2
    if SearchArray[0][mid] ==  SearchValue:
      return mid
    else:
      if SearchArray[0][mid] > SearchValue:
        return BinarySearch(SearchArray,Lower,mid-1,SearchValue)
      else:
        return BinarySearch(SearchArray,mid+1,Upper,SearchValue)        
  return -1

x = BinarySearch(NumberArray,0,ArrayLength,1)
print(x)

f = BinarySearch(NumberArray,0,ArrayLength,-1)
print(f)