# DECALRE ArrayNodes : ARRAY [0,19] OF INTEGER
# DECLARE RootPointer,FreeNode : INTEGER


FreeNode = 0
RootPointer = -1
ArrayNodes = [[-1,0,-1] for index in range(20)]


def AddNode(Array,RootPointer,FreeNode):
    nodeData = int(input("Enter the data you have to insert : "))
    if FreeNode <= 19:
      Array[FreeNode][0] = -1
      Array[FreeNode][1] = nodeData
      Array[FreeNode][2] = -1
      if RootPointer == -1:
        RootPointer = 0
      else:
         placed = False
         currentNode = RootPointer
         while placed == False:
            if nodeData < Array[currentNode][1]:
              if Array[currentNode][0] == -1 :
                 Array[currentNode][0] = FreeNode
                 placed = True
              else:
                 currentNode = Array[currentNode][0]
            else:
               if Array[currentNode][2] == -1:
                 Array[currentNode][2] = FreeNode
                 placed = True
               else:
                  currentNode = Array[currentNode][2]  
      FreeNode += 1
    else:
     print("Tree is full")    
    return Array,RootPointer,FreeNode 

def PrintAll(ArrayNodes):
 for index in range(10):
   print(f"{ArrayNodes[index][0]}  {ArrayNodes[index][1]} {ArrayNodes[index][2]}")


for i in range(10):
  x = AddNode(ArrayNodes,RootPointer,FreeNode)
  ArrayNodes = x[0]
  print(ArrayNodes)
  RootPointer = x[1]
  print(RootPointer)
  FreeNode = x[2]
  print(FreeNode)

# PrintAll(ArrayNodes)      

# def InOrder(ArrayNodes,RootPointer):
#   if ArrayNodes[RootPointer][0] != -1 :
#     InOrder(ArrayNodes,RootPointer)
#   print(ArrayNodes[RootPointer][2])
#   if ArrayNodes[RootPointer][2] != -1 :
#     InOrder(ArrayNodes,ArrayNodes[RootPointer][2])  



def InOrder(ArrayNodes, RootNode):
 if ArrayNodes[RootNode][0] != -1:
    InOrder(ArrayNodes, ArrayNodes[RootNode][0])
 print(str(ArrayNodes[RootNode][1]))
 if ArrayNodes[RootNode][2] != -1:
    InOrder(ArrayNodes, ArrayNodes[RootNode][2]) 
InOrder(ArrayNodes,RootPointer)