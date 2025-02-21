class Character :
    # DECLARE NAME : STRING
    # DECLARE XCoordinate : INTEGER
    # DECLARE YCoordinate : INTEGER

    def __init__(self, name, XCordinate , YCordinate):
      self.name = name
      self.XCoordinate = XCordinate
      self.YCoordinate = YCordinate

    def GetName(self):
       return self.name

    def GetX(self):
        return self.XCoordinate
    
    def GetY(self):
        return self.YCoordinate
    
    def ChangePostion(self,xChange,yChange):
       self.XCoordinate += xChange
       self.YCoordinate += yChange


CharacterArray = [Character("",0,0) for index in range(0,10)]


myFile = open('PYTHON COLLEGE copy/Object Programming/ONLY OOP/Characters.txt', 'r')

for index in range(10):
    name = myFile.readline().strip()
    Xcords = int(myFile.readline().strip())
    Ycords = int(myFile.readline().strip())
    CharacterArray[index] = Character(name,Xcords,Ycords)


# print(CharacterArray[0].GetName())
# print(CharacterArray[1].__dict__)
print(CharacterArray[9].__dict__)


nameToSearch = input("Enter a name you have to search : " )
Found = False
count = 0
foundIndex = -1 

while Found == False:
    for index in range(0,10):
        print(CharacterArray[index].GetName())
        if CharacterArray[index].GetName() == nameToSearch:
            Found = True
            break 
    
    if Found == False:
      nameToSearch = input("Name does not exists please enter a name you have to search : " )
       


Letters = ["A","W","S","D"]
move = input("Enter the direction for which you have to move W for up , S for down , A  for left , D for right : ").upper()
print(move)
while move in Letters:
    if move == "W" :
        CharacterArray[foundIndex].ChangePostion(0,1)
    if move == "A" :
        CharacterArray[foundIndex].ChangePostion(-1,0)
    if move == "S" :
        CharacterArray[foundIndex].ChangePostion(0,-1)
    if move == "D" :
        CharacterArray[foundIndex].ChangePostion(1,0)

    move = input("Enter the direction for which you have to move W for up , S for down , A  for left , D for right : ").upper()


print(f"{nameToSearch} has changed cordinates to X = {CharacterArray[foundIndex].GetX()} and Y = {CharacterArray[foundIndex].GetY()}")