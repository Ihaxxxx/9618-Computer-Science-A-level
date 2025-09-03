# DECLARE Animal ARRAY [1:20] OF STRING
# DECLARE Colour ARRAY [1:10] OF STRING
# DECLARE AnimalTopPointer , ColourTopPointer : INTEGER

AnimalTopPointer = 0
ColourTopPointer = 0
Animal = [""] * 20
Colour = [""] * 10


def PushAnimal(DataTOPush):
    global AnimalTopPointer
    global Animal
    if AnimalTopPointer == 20:
      return False
    else:
      Animal[AnimalTopPointer] = (DataTOPush) 
      AnimalTopPointer += 1
    #   print(AnimalTopPointer)
      return True


def PopAnimal():
 global AnimalTopPointer
 if AnimalTopPointer == 0 :
   return ""
 else:
   ReturnData = Animal[AnimalTopPointer-1]
   AnimalTopPointer -= 1
   return ReturnData



def PushColor(DataTOPush):
    global ColourTopPointer
    global Colour
    if ColourTopPointer == 20:
      return False
    else:
      Colour[ColourTopPointer] = (DataTOPush) 
      ColourTopPointer += 1
      return True


def PopColor():
 global ColourTopPointer   
 if ColourTopPointer == 0 :
   return ""
 else:
   ReturnData = Colour[ColourTopPointer-1]
   ColourTopPointer -= 1
   return ReturnData





def ReadData():
    try:
      myFileAnimal = open("/Users/apple/Documents/A2/COMPUTER SCIENCE/PYTHON COLLEGE/Filling/Text Files - P4/AnimalData.txt","r")
      myFileColor = open("/Users/apple/Documents/A2/COMPUTER SCIENCE/PYTHON COLLEGE/Filling/Text Files - P4/ColourData.txt","r")
      infoAnimal = myFileAnimal.readline().strip()
      infoColor = myFileColor.readline().strip()
      while infoAnimal != "" :
        PushAnimal(infoAnimal)
        infoAnimal = myFileAnimal.readline().strip()
      while infoColor != "" :
        PushColor(infoColor)
        infoColor = myFileColor.readline().strip()  
    except:
      print('An exception occurred')
    print(Animal)  
    print(Colour)
    
# ReadData()    

def OutputItem():
    PopAnimalName = PopAnimal()
    PopColorData = PopColor() 
    if PopAnimalName != "" and PopColorData != "" :
        print(PopAnimalName,PopColorData)
    elif PopAnimalName == "" :
        PushColor(PopColorData)
        print("No Animal")
    elif PopColorData == "":
        PushAnimal(PopAnimalName)
        print("No Colour")
    print(Animal,Colour)
        

ReadData()    
OutputItem()
OutputItem()
OutputItem()
OutputItem()
