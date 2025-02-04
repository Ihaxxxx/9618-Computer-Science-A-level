class Balloon :
    # PRIVATE Health : INTEGER
    # PRIVATE Colour : STRING
    # PRIVATE DefenceItem : STRING
    def __init__(self, defenceItem, colour):
      self.__defenceItem = defenceItem
      self.__colour = colour
      self.__health = 100

    def ChangeHealth(self,health):
        self.__health += health


    def GetDefenceItem(self):
        return self.__defenceItem
    
    def CheckHealth(self):
        if (self.__health <= 0 ):
            return True
        else :
            return False

    def __str__(self):
        return f"Balloon(Colour: {self.__colour}, DefenceItem: {self.__defenceItem}, Health: {self.__health})"        


def Defend(obj,strenght):
    obj.ChangeHealth(-strenght)
    x = obj.GetDefenceItem() 
    print(x)
    y = obj.CheckHealth()
    print(y)
    if y :
      print("Your defence item has no health left")
    else:
        print("Your defence item still has a health")

defenceItem =  input("Enter Your Defence Item : ")
Colour =  input("Enter Your colour : ")
OppStrenght = int(input("Enter the strenght of your opponent"))

Balloon1 = Balloon(defenceItem,Colour)


Defend(Balloon1,OppStrenght)


