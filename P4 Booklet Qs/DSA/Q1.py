# DECLARE myList : ARRYA [0:9] OF INTEGER
myList = [10,5,6,7,1,12,13,15,21,8]
# valuetoseacrh = int(input("enter the number you have to search: "))


# for item in range(0,len(myList)):
#  if myList[item] == valuetoseacrh:

#    print("Value found on the index" , item)
#    found = True  

# if found == False :
#   print("Not found")


# while index < 10 and found == False:
#   if myList[index] == valuetoseacrh :
#     found = True
#   else:
#       index += 1  
      
# if found == True:
#   print("Found at index" , index)
# else:
#     print("Not Found")       
    
    
# def linerSearch(value):
    
#     global myList 
#     index = 0 
#     found = False
    
#     while index < 10 and found == False :
#         if myList[index] == value :
#             return True
#         else:
#             index += 1  
            
#     return False

# x = linerSearch(valuetoseacrh)            
# if x == True:
#   print("Number found")
# else:
#     print("Not Found")

def BubbleSort():
  global myList 
  for i in range(10-1):
     for j in range(9-i):
      if myList[j] < myList[j+1]:
        temp = myList[j]
        myList[j] = myList[j+1]
        myList[j+1] = temp
    

BubbleSort()
print(myList)



# YT Video

# May/June 2021/41 Q2

# DECLARE myList : ARRYA [0:9] OF INTEGER

# myList = [0] * 10
# myList[0] = 10
# myList[1] = 5
# myList[2] = 6 
# myList[3] = 7
# myList[4] = 1
# myList[5] = 12
# myList[6] = 13
# myList[7] = 15
# myList[8] = 21
# myList[9] = 8

# def linerSearch(value):
    
#     global myList 
#     index = 0 
#     found = False
    
#     while index < 10 and found == False :
#         if myList[index] == value :
#             return True
#         else:
#             index += 1  
            
#     return False

# valuetoseacrh = int(input("enter the number you have to search: "))

# returnVal = linerSearch(valuetoseacrh)            
# if returnVal == True:
#   print("Number found")
# else:
#     print("Not Found")
