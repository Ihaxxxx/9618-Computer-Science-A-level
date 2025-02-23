class Vehicle :
    # PRIVATE ID : STRING 
    # PRIVATE MaxSpeed,CurrentSpeed,IncreaseAmount,HorizontalPostion : INTEGER

    def __init__(self, ID, MaxSpeed , IncreaseAmount):
      self.__ID = ID
      self.__MaxSpeed = MaxSpeed
      self.__IncreaseAmount = IncreaseAmount
      self.__CurrentSpeed = 0
      self.__HorizontalPostion = 0


    def SetCurrentSpeed(self,speed):
      self.__CurrentSpeed = speed

    def SetHorizontalPosition(self,position):
      self.__HorizontalPostion = position

    def GetCurrentSpeed(self):
         return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
         return self.__IncreaseAmount
    
    def GetHorizontalPostion(self):
         return self.__HorizontalPostion
    
    def GetMaxSpeed(self):
         return self.__MaxSpeed
    
    def IncreaseSpeed(self,increaseSpeed):
        self.__CurrentSpeed += increaseSpeed
        self.__HorizontalPostion += self.__CurrentSpeed



class Helicopter(Vehicle):
    # PRIVATE VerticalPosition,VerticalChange,MaxHeight : INTEGER 

    def __init__(self,vChange,maxheight):
        super().__init__()
        self.__VerticalChange = vChange
        self.__MaxHeight = maxheight

    def GetVerticalPostion(self):
        return self.__VerticalPosition     
    
    
#     POLU
