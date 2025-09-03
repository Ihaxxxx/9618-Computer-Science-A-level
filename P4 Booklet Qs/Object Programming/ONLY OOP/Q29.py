class Character:
    # DECLARE NAME : STRING
    # DECLARE XPosition,XPosition : INTEGER
    
    def __init__(self,name,XPosition,YPosition):
        self.name = name
        self.XPosition = XPosition
        self.YPosition = YPosition
        
    def SetXPosition(self,position):    
        if position >= 0 and position <= 10000:
            self.XPosition += position
            if self.XPosition > 10000:
              self.XPosition = 10000
            if self.XPosition < 0:
              self.XPosition = 0
        else:
            print("Invalid Position")
 
    def SetYPosition(self,position):    
        if position >= 0 and position <= 10000:
            self.YPosition += position
            if self.YPosition > 10000:
              self.YPosition = 10000
            if self.YPosition < 0:
              self.YPosition = 0
        else:
            print("Invalid Position")
                
        
    def GetXPosition(self):
     return self.XPosition
 
    def GetYPosition(self):
     return self.YPosition
    
    def Move(self,direction):
     if direction == "up":  
        self.SetYPosition(10) 
        return True
     elif direction == "down":
        self.SetYPosition(-10) 
        return True
     elif direction == "left":
        self.SetXPosition(-10) 
        return True
     elif direction == "right":
        self.SetXPosition(10) 
        return True
     else:
        return False  


class BikeCharacter(Character):
    
    def __init__(self,name,XPosition,YPosition):
        super().__init__(name,XPosition,YPosition)

    def Move(self,direction):
     if direction == "up":  
        self.SetYPosition(20)
        return True
     elif direction == "down":
        self.SetYPosition(-20) 
        return True
     elif direction == "left":
        self.SetXPosition(-20) 
        return True
     elif direction == "right":
        self.SetXPosition(20) 
        return True
     else:
        print("Invalid Direction")    
        return False

Jack = Character("Jack",50,50)         
Karla = BikeCharacter("Karla",100,50)


player = input("Enter whom you want to move Jack or Karla : ")

if player == "jack":
  direction = input("Enter the direction you want to move 'up','down','right','left' : " )
  x = Jack.Move(direction)
  if x:
    print(f"Jack's new position is X = {Jack.GetXPosition()} and Y = {Jack.GetYPosition()}")
  else:
      print("invalid direction")  
elif player == "karla":
  direction = input("Enter the direction you want to move 'up','down','right','left' : " )
  x = Karla.Move(direction)
  
  if x:
    print(f"Jack's new position is X = {Karla.GetXPosition()} and Y = {Karla.GetYPosition()}") 
  else:
    print("invalid direction")  
else:
    print("Invalid Name")  