Queue = [0]*100
HeadPointer = -1 
TailPointer = -1


def Enqueu(data):
    global Queue,HeadPointer,TailPointer
    if HeadPointer == 0 and TailPointer == 99:
      return False
    elif HeadPointer == -1 and TailPointer == -1 :
       HeadPointer = 0
       TailPointer = 0
    else:
        TailPointer += 1
    Queue[TailPointer] = data
    return True

for item in range(1,21):
    x = Enqueu(item)

if x :
   print("Successful")
else:
   print("Unsuccessful")

Total = 0
def IterativeOutput(start):
 global HeadPointer,Queue,Total
 Total += Queue[start]
 while start !=  0 :
    return IterativeOutput(start-1) 
 return Total 



# print(sum(Queue))
# print(TailPointer,HeadPointer)

m = IterativeOutput(TailPointer)
print(m)      