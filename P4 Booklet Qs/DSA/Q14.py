global Queue
global HeadPointer
global TailPointer

Queue = []
HeadPointer = -1
TailPointer = 0


def Enqueue(Data):
    global TailPointer
    global HeadPointer
    global Queue

    if TailPointer == 50:
        print("Queue full")
    else:
        Queue.append(Data)
        TailPointer += 1

        if HeadPointer == -1:
            HeadPointer = 0

def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer

    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("Queue empty")
        return "Empty"
    else:
        HeadPointer += 1
        return Queue[HeadPointer - 1]


Enqueue(10)
Enqueue(20)
Enqueue(30)

print("Dequeued:", Dequeue())
print("Dequeued:", Dequeue())

Enqueue(40)
Enqueue(50)


print("Final Queue Array:", Queue)
print("HeadPointer:", HeadPointer)
print("TailPointer:", TailPointer)