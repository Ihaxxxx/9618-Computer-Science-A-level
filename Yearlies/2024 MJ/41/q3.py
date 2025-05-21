QueueHead = -1
QueueTail = -1
QueueData = ["" for index in range(20)]
count = 0


def Enqueue(dataToInsert):
    global QueueHead,QueueTail,QueueData
    if QueueHead == -1 and QueueTail == -1 :
        QueueHead = 0
        QueueTail = 0
        QueueData[QueueTail] = dataToInsert
        return True
    elif QueueTail == 19:
        return True
    
def Dequeue():
    global QueueHead,QueueTail,QueueData
    if QueueHead == -1 and QueueTail == -1:
        return "false"
    else:
        QueueHead += 1
        return QueueData[QueueHead-1]
    
def StoreItems():
    global count
    for index in range(10):
        UserInput = input("Enter a number of 7 characters : ")
        checkdigitValue = (int(UserInput[0])*1 + int(UserInput[1])*3 + int(UserInput[2])*1 + int(UserInput[3])*3 + int(UserInput[4])*1 + int(UserInput[5])*3)//10
        if checkdigitValue == 10:
            checkdigitValue = "X"
        print(UserInput[-1])
        if UserInput[-1] == str(checkdigitValue):
            print("valid")
            count += 1
            Enqueue(UserInput)
    print(f"The amount of valid inputs are {count}")        
            
StoreItems()   