Animal = [""] * 20
Color = [""] * 10

AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global Animal , AnimalTopPointer
    if AnimalTopPointer == 20 :
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True

def PopAnimal():
    global Animal , AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData

PushAnimal("A")
PushAnimal("B")
PushAnimal("C")
PopAnimal()
PopAnimal()
PushAnimal("D")

for item in Animal:
    if item != "":
        print(item)
