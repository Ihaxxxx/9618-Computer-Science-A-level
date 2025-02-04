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
    for i in range(10-1):
       for j in range(9-i):
        if myList[j] < myList[j+1]:
          temp = myList[j]
          myList[j] = myList[j+1]
          myList[j+1] = temp
    
    # return arr

BubbleSort()
print(myList)