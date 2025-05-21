class Node :
    # DECLARE LeftPointer , Data , RightPointer : INTEGER 

    def __init__(self,data):
        self.__data = data
        self.__LeftPointer = -1 
        self.__RightPointer = -1

    def GetLeft(self):
        return self.__data    
    
    def GetRight(self):    
        return self.__LeftPointer
    
    def GetData(self):  
        return self.__RightPointer
    
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
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            CurrentPointer = self.__FirstNode
            while CurrentPointer != 0:
              previousPointer =  CurrentPointer
              if self.__Tree[self.NumberNodes].GetData() > self.__Tree[CurrentPointer].GetData():
                CurrentPointer = self.__Tree[CurrentPointer].GetRight()
                turnRight = True
            else:
              CurrentPointer = (self.__Tree[CurrentPointer]).GetLeft()
              turnRight = False
            if turnRight == True:
                self.__Tree[previousPointer].SetRight(self.__NumberNodes)
            else:
                self.__Tree[previousPointer].SetLeft(self.__NumberNodes)

    def OutputTree(self):
        print("Left Pointer - "+ "Data" + " - Right Pointer")
        for item in self.__Tree[:self.__NumberNodes] :
            print(f"{item.GetLeft()} - {item.GetData()} - {item.GetRight()}" )



TheTree  = TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(7)
TheTree.InsertNode(15)
