class Card:
    # PRIVATE Number : INTEGER
    # PRIVATE Colour : STRING 
    def __init__(self, Number, Color):
      self.__Number = Number
      self.__Color = Color

    def GetNumber(self):
        return self.__Number
    
    def GetColor(self):
        return self.__Color


CardList = [Card(0," ") for index in range(30)]



myFile = open('P4 Booklet Qs/Object Programming/ONLY OOP/CardValues.txt', 'r')

for item in range(30):
    Number = int(myFile.readline().strip())
    Color = myFile.readline().strip()
    record = Card(Number,Color)
    CardList[item] = record
    


seletedCards = []
def ChooseCard():
 global CardList
 global seletedCards
 selected = False

 number = int(input("Enter a card number : "))
 
 while number < 1 or number > 30:
   print("You need to enter a number between 1 and 30")
   number = int(input("Enter A Value Between 1 and 30 inclusive : "))  
 print("Valid")
 
 while selected == False:
        seletedCard = CardList[number-1]
        if seletedCard in seletedCards:
            print("This card is already selected Please Enter Another One")
            number = int(input("Enter A Value Between 1 and 30 inclusive : "))
        else:
            selected = True
            seletedCards.append(seletedCard)

 return number - 1

Player1 = []

for index in range(0,4):
 ReturnNumber = ChooseCard()
 Player1.append(CardList[ReturnNumber])
 

for index in Player1:
    print(index.GetNumber())
    print(index.GetColor())




    
