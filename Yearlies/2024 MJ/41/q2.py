class Tree :
    # DECLARE PRIVATE TreeName : STRING
    # DECLARE PRIVATE HeightGrow : INTEGER
    # DECLARE PRIVATE MaxHeight : INTEGER
    # DECLARE PRIVATE MaxWidth : INTEGER
    # DECLARE PRIVATE Evergreen : STRING
    
    def __init__(self,TreeName,HeightGrow,MaxHeight,MaxWidth,Evergreen):
      self.__TreeName = TreeName
      self.__HeightGrow = HeightGrow
      self.__MaxHeight = MaxHeight
      self.__MaxWidth = MaxWidth
      self.__Evergreen = Evergreen
      
    def GetTreeName(self) :
        return self.__TreeName   
    
    def GetHeightGrow(self) :
        return self.__HeightGrow   
    
    def GetMaxHeight(self) :
        return self.__MaxHeight   
    
    def GetMaxWidth(self) :
        return self.__MaxWidth   
    
    def GetEverGreen(self) :
        return self.__Evergreen   

def ReadData():
        TreeArray = [Tree("",0,0,0,"") for index in range(9)]
        try:
            myFile = open("/Users/apple/Documents/A2/COMPUTER SCIENCE/9618-Computer-Science-A-level/Yearlies/2024 MJ/41/Trees.txt","r")
            info = myFile.readline().strip()
            count = 0 
            while info != "":
                splitedValues = info.split(",")
                TreeArray[count] = Tree(splitedValues[0],int(splitedValues[1]),int(splitedValues[2]),int(splitedValues[3]),splitedValues[4]) 
                count += 1
                info = myFile.readline().strip()
            return TreeArray
        except:
            print("File couldnt be found")


def PrintTrees(Array):
    for index in range(len(Array)):
        if Array[index].GetEverGreen() == "Yes":
            print(f"{Array[index].GetTreeName()} has a maximum height of {Array[index].GetMaxHeight()} a maximum width of {Array[index].GetMaxWidth()} and grows {Array[index].GetHeightGrow()} cm a year. It does not lose it leaves ")
        else:
            print(f"{Array[index].GetTreeName()} has a maximum height of {Array[index].GetMaxHeight()} a maximum width of {Array[index].GetMaxWidth()} and grows {Array[index].GetHeightGrow()} cm a year. It does not lose it leaves each year ")    
        
        
def ChooseTrees(Array):
    maxHeight = int(input("Enter the maximum height of tree you want : "))
    maxWidth = int(input("Enter the maximum width of tree you want : "))
    everGreen = input("Enter your condition for being ever green (yes/no) : ").lower()
    userReqArray = []
    for index in range(len(Array)):
        if Array[index].GetMaxHeight() <= maxHeight and Array[index].GetMaxWidth() <= maxWidth and Array[index].GetEverGreen().lower() == everGreen :
            userReqArray.append(Array[index])
    if len(userReqArray) == 0:
        print("Sorry there arent any trees which are upto the mark for your requrirements")
    else:        
        PrintTrees(userReqArray)    
    TreeName = input("The name of the tree that you want to buy : ")
    InitialHeight = int(input("Enter the initial height of the tree : "))
    print(userReqArray[0].GetTreeName() == TreeName)
    for index in range(len(userReqArray)-1):
        if userReqArray[index].GetTreeName() == TreeName :
            timeTaken = (userReqArray[index].GetMaxHeight() - InitialHeight) // userReqArray[index].GetHeightGrow()
            print(f"The tree will take {timeTaken} years to reach its maximum height of {userReqArray[index].GetMaxHeight()}")
            
        
x = ReadData()
ChooseTrees(x)

# print(type(x[0].GetMaxWidth()))