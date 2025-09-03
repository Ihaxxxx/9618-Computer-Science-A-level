# DECALRE QUEUE :  ARRAY [0:49] OF STRING
# DECLARE HeadPointer , TailPointer : INTEGER 

class RecordData :
  def __init__(self, ID, Total):
    self.ID = ID
    self.Total = Total



Queue = [""]*50
HeadPointer = -1
TailPointer = 0

def Enqueu(data):
 global Queue,HeadPointer,TailPointer
 if (HeadPointer == 0 and TailPointer == 49) or (HeadPointer == TailPointer + 1) :
   print("Queue is full")
   return
 
 if HeadPointer == -1 :
   HeadPointer = 0
   TailPointer = 0
 elif TailPointer == 49 :
    TailPointer = 0 
 else:
   TailPointer += 1
   
 Queue[TailPointer] = data
 print("Queue upadated")
   
    
def DeQueue():
  global Queue,HeadPointer,TailPointer
  if HeadPointer == -1 :
    print("Empty")
  else:
    data = Queue[HeadPointer]
    if HeadPointer == TailPointer:
      HeadPointer = -1
      TailPointer = -1
    elif HeadPointer == 49 :
      HeadPointer = 0
    else:
      HeadPointer += 1
  return data      


def ReadData():
    global Queue
    myFile = open('D:\A level\9618-Computer-Science-A-level\PYTHON COLLEGE copy\Object Programming\RECORD\QueueData.txt', 'r')
    info = myFile.readline().strip()
    while info != "":
        Enqueu(info)
        info = myFile.readline().strip()

  

# c
NumberRecords = 0
Records = [RecordData("",0) for index in range(50)]

def TotalData():
    global Records,NumberRecords
    DataAccessed = DeQueue() 
    flag = False
    if NumberRecords == 0:
      Records[NumberRecords].ID = DataAccessed
      Records[NumberRecords].Total = 1
      flag = True
      NumberRecords += 1
    else:
      for X in range(0,NumberRecords-1):
       if Records[X].ID == DataAccessed:
         Records[X].Total += 1  
         flag = True
    if flag == False:
      Records[NumberRecords].ID = DataAccessed
      Records[NumberRecords].Total = 1
      NumberRecords += 1


def OutputRecords():
 for index in range(NumberRecords ):
   print(f"ID {Records[index].ID} Total {Records[index].Total}")

ReadData()

print(Queue)
for item in range(HeadPointer,TailPointer+1):
    TotalData()

OutputRecords()

  

