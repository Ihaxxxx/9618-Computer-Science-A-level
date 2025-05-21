class Node :
    # DECLARE LeftPointer , Data , RightPointer : INTEGER 

    def __init__(self,data):
        self.__data = data
        self.__LeftPointer = -1 
        self.__RightPointer = -1

    def GetLeft(self):
        return self.__LeftPointer
    
    def GetRight(self):    
        return self.__RightPointer
    
    def GetData(self):  
        return self.__data
    
    def SetLeft(self,value):
        self.__LeftPointer = value
    def SetRight(self,value):
        self.__RightPointer = value
    def SetData(self,value):
        self.__data = value


class TreeClass:
    # DECLARE TREE ARRAY OF [0:19] OF NODE
    # DECLARE FirstNode,NumberNode : INTEGER
    def __init__(self):
        self.__Tree = [Node(-1) for i in range(20)]
        self.__FirstNode = -1
        self.__NumberNodes = 0

    def InsertNode(self,NewNode):
        if self.__FirstNode == -1 :
            self.__FirstNode = 0
            self.__Tree[self.__NumberNodes].SetData(NewNode)
            self.__NumberNodes += 1

            CurrentPointer = self.__FirstNode

            while True:
                PreviousPointer = CurrentPointer
                if self.__Tree[newIndex].GetData() > self.__Tree[CurrentPointer].GetData():
                    CurrentPointer = self.__Tree[CurrentPointer].GetRight()
                    turnRight = True
                else:
                    CurrentPointer = self.__Tree[CurrentPointer].GetLeft()
                    turnRight = False

                if CurrentPointer == -1:
                    if turnRight:
                        self.__Tree[PreviousPointer].SetRight(newIndex)
                    else:
                        self.__Tree[PreviousPointer].SetLeft(newIndex)
                    break

    def OutputTree(self):
        print("Left - Data - Right")
        for i in range(self.__NumberNodes):
            item = self.__Tree[i]
            print(f"{item.GetLeft()} - {item.GetData()} - {item.GetRight()}")



TheTree  = TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()