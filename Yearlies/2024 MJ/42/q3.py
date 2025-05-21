
# DECLARE NumberArray [1,6] OF INTEGER
NumberArray = [0]*7
NumberArray[0] = 100
NumberArray[1] = 85
NumberArray[2] = 644
NumberArray[3] = 22 
NumberArray[4] = 15
NumberArray[5] = 8
NumberArray[6] = 1

print(NumberArray)

# DECLARE LastItem : INTEGER
# DECLARE CheckItem : INTEGER
# DECLARE LoopAgain : BOOLEAN

def RecursiveInsertion(integerarray,NumberElements):
    if NumberElements <= 1 :
     return integerarray
    else:
        RecursiveInsertion(integerarray,NumberElements-1)
        LastItem = integerarray[NumberElements-1]
        CheckItem = NumberElements-2
    loopAgain = True
    if CheckItem < 0:
      loopAgain = False
    else:
       if integerarray[CheckItem] < LastItem :
          loopAgain = False
    while loopAgain:
       integerarray[CheckItem+1] = integerarray[CheckItem]
       CheckItem = CheckItem - 1
       if CheckItem < 0 :
          loopAgain = False
       else:
          if integerarray[CheckItem] < LastItem:
             loopAgain = False
    integerarray[CheckItem+1] = LastItem
    return integerarray
           
RecursiveInsertion(NumberArray,len(NumberArray))                     
print("Recursive")
print(NumberArray)

def IterativeInsertion(integerarray,NumberElements) :
    for index in range(1,NumberElements-1):
        itemTobeInserted = integerarray[index]
        key = index - 1
        while itemTobeInserted < integerarray[key] and key > 0 :
           NumberArray[key + 1] = NumberArray[key]
           key = key -1 
        NumberArray[key + 1] = itemTobeInserted

IterativeInsertion(NumberArray,len(NumberArray)) 
print("Iterative")
print(NumberArray)

def binarySearch(integerarray,firstIndex,lastIndex,ToFind):
    if firstIndex > lastIndex :
      return -1
    middle = int((lastIndex+firstIndex)/2)
    if integerarray[middle] == ToFind:
       return middle
    elif ToFind > integerarray[middle]:
       return binarySearch(integerarray,middle+1,lastIndex,ToFind)
    elif ToFind < integerarray[middle]:
       return binarySearch(integerarray,firstIndex,middle-1,ToFind)


x = binarySearch(NumberArray,0,len(NumberArray)-1,4 )
if x == -1:
   print("Not Found")
else:
   print(f"The number 644 is found on index {x}")      