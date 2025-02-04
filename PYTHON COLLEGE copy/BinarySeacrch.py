# DECLARE myList : ARRYA [0:9] OF INTEGER
myList = [5,18,27,34,48,55,62,71,88,94]




def binarySeacrh(seacrhNumber):
 global myList
 top = 0
 bottom = 9
 found = False
 
 while (top <= bottom):
   middle = int((top + bottom)/2)
   if seacrhNumber == myList[middle]:
     return middle
    # found = true
   elif seacrhNumber > myList[middle]:
     top = middle + 1
   else:
     bottom = middle - 1
 return -1 


searchNum = int(input("Enter the value You have to seacrh: "))
x = binarySeacrh(searchNum)
if x != -1:
  print("Number found at index",x)
else:
  print("Number not found")