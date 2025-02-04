# DECLARE DataArray : ARRAY [] OF INTEGER

DataArray = []

myFile = open("/Users/apple/Documents/A2/COMPUTER SCIENCE/PYTHON COLLEGE/Filling/Text Files - P4/Data.txt","r")

for item in range(25):
    info = myFile.readline().strip()
    DataArray.append(int(info))
    
myFile.close()
print(DataArray)


def PrintArray(Array):
    for item in DataArray:
        print(item, end=" ")
  
# PrintArray(DataArray)  



num = int(input("Enter a Number between 0 and 100 inclusive :"))
while (num > 100 or num < 0) :
    num = int(input(("Enter a Number between 0 and 100 inclusive")))
    print(num)
    
def linearSearch(value,Array):
    found = False
    index = 0    
    count = 0 
    while index < 25 and found == False :
            if Array[index] == value :
                count += 1
                index += 1 
            else:
                index += 1  
                
    return count
 
print("The number ",num," is Found ",linearSearch(num,DataArray)," times")        