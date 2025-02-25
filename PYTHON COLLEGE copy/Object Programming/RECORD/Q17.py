class node:
 def __init__(self):
  self.data = 0
  self.nextNode = 0
  
startPointer = 0
emptyList = 5  
  
LinkedList = [node() for index in range(10)]  
  
LinkedList[0].data     = 1
LinkedList[0].nextNode = 1
LinkedList[1].data     = 5
LinkedList[1].nextNode = 4
LinkedList[2].data     = 6
LinkedList[2].nextNode = 7
LinkedList[3].data     = 7
LinkedList[3].nextNode = -1
LinkedList[4].data     = 2
LinkedList[4].nextNode = 2
LinkedList[5].data     = 0
LinkedList[5].nextNode = 6
LinkedList[6].data     = 0
LinkedList[6].nextNode = 8
LinkedList[7].data     = 56 
LinkedList[7].nextNode = 3
LinkedList[8].data     = 0
LinkedList[8].nextNode = 9
LinkedList[9].data     = 0
LinkedList[9].nextNode = -1




def OutputNodes(array,startPointer):
    print(array[startPointer].data)
    while array[startPointer].nextNode != -1:
      return OutputNodes(array,array[startPointer].nextNode)

def addNode(linkedList,startPointer,emptylist):
    if emptylist != -1 :
        data = int(input("Enter a new number : "))
        linkedList[emptylist].data = data
        temp = emptylist
        
        currentPointer = startPointer
        while currentPointer != -1:
            previouspointer = currentPointer
            currentPointer = linkedList[previouspointer].nextNode
        
        linkedList[previouspointer].nextNode = emptylist
        emptylist = linkedList[emptyList].nextNode            
        linkedList[temp].nextNode = -1
        return True
    else:
        return False
        
 



OutputNodes(LinkedList,startPointer)      
x = addNode(LinkedList,startPointer,emptyList)
if x:
  print("Item is added")
else:
  print("Linked list is full")
  
OutputNodes(LinkedList,startPointer)      