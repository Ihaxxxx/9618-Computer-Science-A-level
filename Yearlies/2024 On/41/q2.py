class Horse:
    # DECLARE Name : STRING
    # DECLARE MaxFenceHeight , PercentageSuccess : INTEGER

    def __init__(self, name, MaxFenceHeight,PercentageSuccess):
      self.__Name = name
      self.__MaxFenceHeight = MaxFenceHeight
      self.__PercentageSuccess = PercentageSuccess

    def GetName(self):
       return self.__Name   
    
    def GetMaxFenceHeight(self):
       return self.__MaxFenceHeight
    
    def Success(self,height,risk):
       if height > self.__MaxFenceHeight :
          return self.__PercentageSuccess * 0.2
       elif height <= self.__MaxFenceHeight:
          match risk:
             case 1:
                return  self.__PercentageSuccess * 1
             case 2:
                return  self.__PercentageSuccess * 0.9
             case 3:
                return  self.__PercentageSuccess * 0.8
             case 4:
                return  self.__PercentageSuccess * 0.7
             case 5:
                return  self.__PercentageSuccess * 0.6

class Fence:
    #    DECLARE Height, Risk : INTEGER
    def __init__(self, Height, Risk):
      self.__Height = Height
      self.__Risk = Risk

    def GetHeight(self):
       return self.__Height
    
    def GetRisk(self):
       return self.__Risk


Horses = []
Horses.append(Horse('Beauty',150,72))
Horses.append(Horse('Jet',160,65))

# for item in Horses:
#    print(item.GetName())

Courses = []

for index in range(4):
   height = int(input(f"Enter the height of {index+1} fence between 70 to 180 inclusive : "))
   while height > 180 or height < 70 :
      height = int(input(f"Invalid {index+1} height enter please enter a height of 70 to 180 inclusive : "))

   Risk = int(input(f"Enter the {index+1} Risk of fence between 1 to 5 inclusive : "))
   while Risk > 5 or Risk < 1 :
      Risk = int(input(f"Invalid {index+1} Risk enter please enter a Risk of 1 to 5 inclusive : "))

   Courses.append(Fence(height,Risk))  

AverageChanceArray = []
for hosNum in range(2):
    TotalChance = 0
    for index in range(4):
       chance = Horses[hosNum].Success(Courses[index].GetHeight(),Courses[index].GetRisk())
       TotalChance += chance
       print(f"The horse {Horses[hosNum].GetName()} at Fence {index + 1} has a {chance} of success")
    print(f"The horse {Horses[hosNum].GetName()} has a average success of {TotalChance/4}")
    AverageChanceArray.append(TotalChance/4)

if AverageChanceArray[0] > AverageChanceArray[1]:
  print(f"The horse {Horses[0].GetName()} has an better average of jumping over all four fences")
else:
   print(f"The horse {Horses[1].GetName()} has an better average of jumping over all four fences")