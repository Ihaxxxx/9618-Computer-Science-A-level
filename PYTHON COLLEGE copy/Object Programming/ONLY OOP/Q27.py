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
    
    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        self.__HorizontalPostion += self.__CurrentSpeed



class Helicopter(Vehicle):
    # PRIVATE VerticalPosition,VerticalChange,MaxHeight : INTEGER 

    def __init__(self, ID, MaxSpeed, IncreaseAmount, vChange, maxHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.__VerticalChange = vChange
        self.__MaxHeight = maxHeight
        self.__VerticalPosition = 0

    def GetVerticalPostion(self):
        return self.__VerticalPosition     
   
    def IncreaseSpeed(self):
          
      if self.__VerticalPosition + self.__VerticalChange < self.__MaxHeight  :
          self.__VerticalPosition += self.__VerticalChange    
      else:
           print("The vertical Position cannot exceed the max height")   
        
    

# def OutputData(vehicle):
     
car = Vehicle("Tiger",100,20)
helicopter  = Helicopter("Lion",350,40,3,100)

print(helicopter.__dict__)
helicopter.IncreaseSpeed()
helicopter.IncreaseSpeed()

print(helicopter.__dict__)