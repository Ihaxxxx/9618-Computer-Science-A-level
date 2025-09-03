QueueData = ["" for index in range(20)]

startPointer = -1
endPointer = -1 

def Enqeue(item):
    global QueueData,startPointer,endPointer
    if ((startPointer == 0 and endPointer == 19) or (startPointer == endPointer + 1)):
      return False
    else:
       if startPointer == -1 and endPointer == -1:
         startPointer = 0
         endPointer = 0
       elif(endPointer == len(QueueData)-1):
          endPointer = 0
       else:
          endPointer += 1  
    QueueData[endPointer] = item
    return True


def ReadFile():
   filename = input("Enter the file name : ")
   try:
     f = open('PYTHON COLLEGE copy/Filling/Text Files - P4/' + filename , 'r')
    #  f = open('PYTHON COLLEGE copy/Filling/Text Files - P4/DataToAdd.txt' , 'r')
    #  f = open('PYTHON COLLEGE copy/Filling/Text Files - P4/SecondData.txt' , 'r')
     info = f.readline().strip()
     while info != "" :
       x = Enqeue(info)
       if x == False:
         return 1
       print(x)
       info = f.readline().strip()
     if x == True:
       return 2
   except:
     return  -1

# functionOut = ReadFile()
# if functionOut == 2:
#   print("All the items are added to the queue")
# elif functionOut == 1 :
#    print("The Queue is full")
# else:
#    print("Text file couldnt be found")   


def Remove():
 global QueueData,startPointer
 if QueueData[startPointer] != "" and QueueData[startPointer+1] != "" :
  var1 = QueueData[startPointer]
  var2 = QueueData[startPointer+1]
  return var1 + " " + var2
 else: 
  return "No Items"

ReadFile()
print(QueueData)
startPointer = endPointer
print(Remove())