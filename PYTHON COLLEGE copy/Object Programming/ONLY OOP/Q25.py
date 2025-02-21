class Card :
    # PRIVATE Number : INTEGER
    # PRIVATE Colour : STRING

    def __init__(self, number, color):
      self.__Number = number
      self.__Color = color
    
    def GetNumber(self):
        return self.__Number
    
    def GetColor(self):
        return self.__Color

class Hand(Card):
    # PRICATE ARRAY CARDS [0,9] OF CARD
    # PRIVATE FirstCard : INTEGER
    # PRIVATE NumberCards : INTEGER
    def __init__(self,card):
      self.__cards = card
      self.__FirstCard = 0
      self.__NumberCards = 5


    def GetCard(self,index):
     return self.__cards[index]



color = ["red","blue","yellow"]
digits = [1,2,3,4,5]
count = 0
CardList = [Card(0," ") for index in range(15)]

for item in color:
 for number in digits:
    record = Card(number,item)
    CardList[count] = record
    count += 1


Player1 = Hand((CardList[0],CardList[1],CardList[2],CardList[3],CardList[10]))
Player2 = Hand((CardList[11],CardList[12],CardList[13],CardList[14],CardList[5]))

def CalculateValue(hand):
   score = 0
   for item in range(5):
    number = hand.GetCard(item).GetNumber()
    color = hand.GetCard(item).GetColor()
    score += number
    if color == "red":
      score += 5
    elif color == "blue":
        score += 10
    else:
       score += 15        
    return score

Player1Score = CalculateValue(Player1)
Player2Score = CalculateValue(Player2)

if Player1Score > Player2Score:
  print("Player 1 Has won")
elif Player1Score < Player2Score:
    print("Player 2 Has won")
else :
   print("There is a draw")     