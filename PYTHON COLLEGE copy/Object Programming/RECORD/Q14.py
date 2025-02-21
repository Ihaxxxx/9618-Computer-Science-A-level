class SaleData:
  def __init__(self, id, qty):
    self.id = id
    self.qty = qty
    
    
CircularQueue = [SaleData("",-1) for index in range(5)]    
head = 0
tail = 0
NumberOfItems = 0



def enqeue(NewRecord):
 global CircularQueue,tail,head,NumberOfItems
 if NumberOfItems == 5:
    return -1
 else:  
    CircularQueue[tail] = NewRecord
    NumberOfItems += 1
    if tail == 4:
      tail = 0
    else:  
        tail += 1
    return 1

def Dequeue():
 global CircularQueue,tail,head,NumberOfItems
 firstRecord = SaleData("",-1)
 if NumberOfItems == 0:
   return firstRecord
 else:
    firstRecord = CircularQueue[head]
    NumberOfItems = NumberOfItems -1 
    if head == 4:
        head = 0
    else:
        head += 1    
    return firstRecord      


def EnterRecord():
        id = input("Enter Your ID ")
        qty = int(input("Enter The quantity "))
        record = SaleData(id.upper(),qty)
        x = enqeue(record)
        if x == -1:
            print("Full")
        else:
            print("Stored")  
    
 



# enqeue(SaleData("Mubashir",1)) 

# x = Dequeue()
# print(x)
for item in range(6):
    EnterRecord()
    
y = Dequeue()

if y.id == "":
  print("Queue is empty")
else:
    print(y.id,y.qty)

EnterRecord()

for item in CircularQueue:
      print(item.id,item.qty)


