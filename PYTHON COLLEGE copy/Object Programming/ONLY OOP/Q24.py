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
seletedCards = []
Player1 = [Card(0," ") for index in range(0,4)]

myFile = open('D:\A level\9618-Computer-Science-A-level\PYTHON COLLEGE copy\Object Programming\CardValues.txt', 'r')

for item in range(30):
    Number = int(myFile.readline().strip())
    Color = myFile.readline().strip()
    record = Card(Number,Color)
    CardList[item] = record
    



def ChooseCard(number):
 global CardList
 global seletedCards
 selected = False

 while selected == False:
        if (number >= 1 and number <= 30):
            seletedCard = CardList[number-1]
            if seletedCard in seletedCards:
                print("This card is already selected Please Enter Another One")
                number = int(input("Enter A Value Between 1 and 30 inclusive : "))
            else:
                selected = True
                seletedCards.append(seletedCard)
                return CardList.index(seletedCard)

for index in range(0,4):
 number = int(input("Enter a card number : "))
 x = ChooseCard(number)
 Player1[index] = CardList[index]

for index in Player1:
    print(index.GetNumber())
    print(index.GetColor())



# print(Player1[0].__dict__)
