class Vehicle :
    # PRIVATE ID : STRING 
    # PRIVATE MaxSpeed,CurrentSpeed,IncreaseAmount,HorizontalPostion : INTEGER

    def __init__(self, ID, MaxSpeed , IncreaseAmount):
      self.__ID = ID
      self.__MaxSpeed = MaxSpeed
      self.__IncreaseAmount = IncreaseAmount
      self.__CurrentSpeed = 0
      self.__HorizontalPosition  = 0


    def SetCurrentSpeed(self,speed):
      self.__CurrentSpeed = speed

    def SetHorizontalPosition(self,position):
      self.__HorizontalPosition  = position

    def GetCurrentSpeed(self):
         return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
         return self.__IncreaseAmount
    
    def GetHorizontalPostion(self):
         return self.__HorizontalPosition 
    
    def GetMaxSpeed(self):
         return self.__MaxSpeed
    
    def IncreaseSpeed(self):
        if self.__CurrentSpeed + self.__IncreaseAmount  <= self.__MaxSpeed:
          self.__CurrentSpeed += self.__IncreaseAmount
        else:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed




class Helicopter(Vehicle):
    # PRIVATE VerticalPosition,VerticalChange,MaxHeight : INTEGER 

    def __init__(self, ID, MaxSpeed, IncreaseAmount, vChange, maxHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.__VerticalChange = vChange
        self.__MaxHeight = maxHeight
        self.__VerticalPosition = 0

    def GetVerticalPosition(self):
        return self.__VerticalPosition     
   
    def IncreaseSpeed(self):
          
      if self.GetCurrentSpeed() + self.GetIncreaseAmount() <= self.GetMaxSpeed()  :
          newSpeed = self.GetCurrentSpeed() + self.GetIncreaseAmount()    
      else:
          newSpeed = self.GetMaxSpeed()   
      
      self.SetCurrentSpeed(newSpeed)
      if self.__VerticalPosition + self.__VerticalChange <= self.__MaxHeight:
          self.__VerticalPosition += self.__VerticalChange
      else:
          self.__VerticalPosition = self.__MaxHeight
      self.SetHorizontalPosition(self.GetHorizontalPostion()+self.GetCurrentSpeed())    

    

def OutputVehicleDetails(vehicle):
    if isinstance(vehicle, Helicopter):
        print(f"Helicopter Details:")
        print(f"  Horizontal Position: {vehicle.GetHorizontalPostion()}")
        print(f"  Vertical Position: {vehicle.GetVerticalPosition()}")
        print(f"  Current Speed: {vehicle.GetCurrentSpeed()}")
    else:
        print(f"Vehicle Details:")
        print(f"  Horizontal Position: {vehicle.GetHorizontalPostion()}")
        print(f"  Current Speed: {vehicle.GetCurrentSpeed()}")

     
car = Vehicle("Tiger",100,20)
helicopter  = Helicopter("Lion",350,40,3,100)

car.IncreaseSpeed()
car.IncreaseSpeed()
OutputVehicleDetails(car)

helicopter.IncreaseSpeed()
helicopter.IncreaseSpeed()
OutputVehicleDetails(helicopter)