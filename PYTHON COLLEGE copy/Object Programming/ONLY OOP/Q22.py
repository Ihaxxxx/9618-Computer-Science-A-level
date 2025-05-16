class Picture :
    # DECLARE Description,FrameColour : STRING
    # DECLARE Width , Height : INTEGER

    def __init__(self,description,Width,Height,FrameColour):
        self.__description = description
        self.__width = Width
        self.__height = Height
        self.__frameColour = FrameColour
    
    def GetDescription(self):
        return self.__description
    
    def GetHeight(self):
        return self.__width
    
    def GetWidth(self):
        return self.__height
    
    def GetFrameColour(self):
        return self.__frameColour
    
    def SetDescription(self,description):
        self.__description = description


PictureArray = [Picture("",0,0,"") for index in range(100)]


def ReadData(PictureArray):
    try:
      myFile = open('D:\A level\9618-Computer-Science-A-level\PYTHON COLLEGE copy\Object Programming\ONLY OOP\Pictures.txt','r')
      count = 0
      for index in range(21):
          description = myFile.readline().strip()
          width = int(myFile.readline().strip())
          height = int(myFile.readline().strip())
          frameColour  = myFile.readline().strip()
          PictureArray[count] = Picture(description,width,height,frameColour)
          count += 1
      myFile.close()
      return count
    except IOError:
      print('An exception occurred')

maxwidth = int(input("Enter the max width by your requiremnets : "))
maxheight = int(input("Enter the the max height by your requiremnets : "))
frameColour = input("Enter the colour of frame by your requiremnets : ").lower()

PictureCount = ReadData(PictureArray)
# print(PictureCount)

for index in range(PictureCount):
 if PictureArray[index].GetFrameColour() == frameColour :
   if PictureArray[index].GetWidth() <= maxwidth :
     if PictureArray[index].GetHeight() <= maxheight:
       print(PictureArray[index].GetDescription(),PictureArray[index].GetFrameColour(),PictureArray[index].GetHeight(),PictureArray[index].GetWidth())