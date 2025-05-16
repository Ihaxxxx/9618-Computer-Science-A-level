# DECLARE DataStored ARRAY [1:20] OF INTEGER
# DECLARE NumberItems : INTGER

DataStored = []
numberItems = 0

def Initialise():
    global DataStored
    NumberItems = int(input("Enter the amount of numbers you want to input between 1 to 20 inclusive : "))
    if NumberItems > 0 and NumberItems <= 20:
        print(NumberItems)
        DataStored = [0 for _ in range(NumberItems)]
        for index in range(NumberItems):
            numberInput = int(input("Enter a integer number : "))
            DataStored[index] = numberInput
    else:
        print("Enter a valid number ")
        

def BubbleSort():
    global DataStored,numberItems
    for i in range(len(DataStored)):
        for j in range(len(DataStored)-1-i):
            if DataStored[j] > DataStored[j+1]:
             temp = DataStored[j]  
             DataStored[j] = DataStored[j+1]
             DataStored[j+1] = temp
    
def BinarySearch(SearchValue):
    global DataStored, numberItems
    print(DataStored)
    top = len(DataStored) - 1 
    lower = 0
    while lower <= top:
        mid = (lower + top) // 2
        if SearchValue == DataStored[mid]:
            return mid
        elif SearchValue > DataStored[mid]:
            lower = mid + 1
        else:
            top = mid - 1
    return -1  
       
           

    
Initialise()        
BubbleSort()
print(DataStored)

valueToFind = int(input("Enter a value you have to find : "))
print(BinarySearch(valueToFind))
