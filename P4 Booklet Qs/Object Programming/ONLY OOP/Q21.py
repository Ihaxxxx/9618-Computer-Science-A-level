class TreasureChest :
    # DECLARE Question : STRING
    # DECLARE answer,points : INTEGER

    def __init__(self,qs,ans,points):
        self.__question = qs
        self.__answer  = ans
        self.__points = points
    def GetQuestion(self):
       return self.__question
    def CheckAnswer(self,answer):
       if self.__answer == answer:
         return True
       else:
          return False
    def getpoints(self,attempts):
       if attempts == 1:
         return self.__points
       elif attempts == 2:
         return int(self.__points/2)
       elif attempts == 3 or attempts == 4:
         return int(self.__points/4)
       else:
          return 0

   
def ReadData():
    arrayTreasure = []
    try:
       myfile = open("D:\A level\9618-Computer-Science-A-level\PYTHON COLLEGE copy\Object Programming\ONLY OOP\TreasureChestData.txt","r")
       qs = myfile.readline().strip()
       while qs != "":
        Ans = int(myfile.readline().strip())
        points = int(myfile.readline().strip())
        arrayTreasure.append(TreasureChest(qs,Ans,points))
        qs = myfile.readline().strip()
       return arrayTreasure
    except:
      print('An exception occurred')



arrayTreasure = ReadData()
# print(arrayTreasure)

qsNum = int(input("Enter question number from 1 to 5 inclusive : "))
while qsNum < 1 or qsNum > 5 :
 qsNum = int(input("Enter a valid question number from 1 to 5 inclusive : "))
   
print(arrayTreasure[qsNum-1].GetQuestion())
print(arrayTreasure[qsNum-1].__dict__)

answer = int(input("Enter the answer for this qs : "))
attempts = 0
valid = arrayTreasure[qsNum-1].CheckAnswer(answer)
attempts += 1
print(valid)
while valid == False and attempts <= 4:
   attempts += 1
   if valid == False:
    answer = int(input("Enter the correct answer for this qs : "))
    valid = arrayTreasure[qsNum-1].CheckAnswer(answer)

points = arrayTreasure[qsNum-1].getpoints(attempts)
print(f"User got this much points {points}")


