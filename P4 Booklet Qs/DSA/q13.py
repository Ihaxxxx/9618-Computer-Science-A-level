#DECLARE QueueArray : ARRAY[0:9] OF STRING
#DECLARE Headpointer,Tailpointer,Noofitems : INTEGER

Headpointer = 0
Tailpointer = 0
Noofitems = 0
QueueArray = [""] *10

def Enqueue(PQueueArray,PHeadpointer,PTailpointer,PNoofitems,PDatatoadd):

    if PNoofitems == 10:
        return (False, PQueueArray, PHeadpointer, PTailpointer, PNoofitems)
    PQueueArray[PTailpointer] = PDatatoadd
    if PTailpointer >= 9:
        PTailpointer = 0
    else:
        PTailpointer = PTailpointer + 1
    PNoofitems = PNoofitems + 1
    return (True, PQueueArray, PHeadpointer, PTailpointer, PNoofitems)

def Dequeue(QueueArray,Headpointer,Tailpointer,Noofitems):

    if Noofitems == 0:
        return (False, QueueArray, Headpointer, Tailpointer, Noofitems)
    else:
        temp = QueueArray[Headpointer]
        Headpointer = Headpointer + 1
        if Headpointer > 9:
            Headpointer = 0
        Noofitems = Noofitems - 1
        return (temp, QueueArray, Headpointer, Tailpointer, Noofitems)


for i in range(0,11):
    data = input("enter your value: ")
    ReturnValue, QueueArray, Headpointer, Tailpointer, Noofitems = Enqueue(QueueArray,Headpointer,Tailpointer,Noofitems,data)
    # ReturnValue, QueueArray, Headpointer, Tailpointer, Noofitems = (True, PQueueArray, PHeadpointer, PTailpointer, PNoofitems)
    if ReturnValue == True:
        print("Addition")
    else :
        print("Unsuccessful")


ReturnValue, QueueArray, Headpointer, Tailpointer, Noofitems = Dequeue(QueueArray,Headpointer,Tailpointer,Noofitems)
print(ReturnValue)
ReturnValue, QueueArray, Headpointer, Tailpointer, Noofitems = Dequeue(QueueArray,Headpointer,Tailpointer,Noofitems)
print(ReturnValue)





