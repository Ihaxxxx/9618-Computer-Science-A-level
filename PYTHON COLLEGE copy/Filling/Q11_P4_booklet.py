# DECLARE StackData ARRAY [1,10] OF INTEGER 
# DECLARE StackPointer : INTEGER

StackData = [0]*10
StackPointer = 0

def OutputData():
    for item in StackData:
        print(item)
    print("Stack Pointer Value",StackPointer)    
# OutputData()

def push(data):
    global StackPointer
    if StackPointer == 10:
        print(f"The stack is full the data {data} cannot be added to the stack as it is full")
        return False
    else:
        StackData[StackPointer] = data
        StackPointer += 1
        print(f"The data {data} is added to the stack")
        return False
    
for i in range(0,11): 
    data = int(input("Enter a number : "))   
    push(data)
# OutputData()

def Pop():
    global StackPointer
    if StackPointer == 0:
        return False
    else:
        StackPointer -= 1
        return StackData[StackPointer]
 
Pop()    
Pop()
OutputData()    