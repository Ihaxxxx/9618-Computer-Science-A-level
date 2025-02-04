# DECLARE DataArray : ARRAY [1:100] OF INTEGER

DataArray = []

myfile = open("/Users/apple/Documents/A2/COMPUTER SCIENCE/PYTHON COLLEGE/Filling/Text Files - P4/IntegerData.txt","r")


def ReadFile():
    global DataArray
    for item in range(100):
        info = myfile.readline().strip()
        DataArray.append(int(info))
    myfile.close()
    print(DataArray) 

ReadFile()

def FindValue():
    global DataArray
    count = 0 
    num = int(input("Enter a number between 0 to 100 inclusive :"))
    while num <0 or num > 100 :
        num = int(input("Enter a number between 0 to 100 inclusive :"))
    for item in DataArray:
        if num == item:
          count += 1 
    print("The Number of times the value ",num,"appear is",count)  
FindValue()


def BubbleSort(): 
    global DataArray
    for i in range(100-1):
       for j in range(99-i):
        if DataArray[j] > DataArray[j+1]:
          temp = DataArray[j]
          DataArray[j] = DataArray[j+1]
          DataArray[j+1] = temp
    print(DataArray)    
   
BubbleSort()   