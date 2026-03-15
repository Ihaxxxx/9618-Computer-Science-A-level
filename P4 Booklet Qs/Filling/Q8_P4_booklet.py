# DECLARE PlayerScoreArray : ARRAY [0:10] OF INTEGER
# DECLARE PlayerNameArray : ARRAY [0:10] OF STRING

PlayerScoreArray = [0]*10
PlayerNameArray = [""]*10

# print(PlayerScore,PlayerName)

def ReadHighScore():
 count = 0    
 myFile = open("P4 Booklet Qs/Filling/Text Files - P4/HighScore.txt","r")
 PlayerName = myFile.readline().strip()
 PlayerScore = myFile.readline().strip()
#  print(PlayerScore,PlayerName)
 while PlayerName != "" or PlayerScore != "" :
    PlayerNameArray[count] = PlayerName
    PlayerScoreArray[count] = int(PlayerScore)
    PlayerName = myFile.readline().strip()
    PlayerScore = myFile.readline().strip()
    count += 1
#  print(PlayerScoreArray,PlayerNameArray)


def OutputHighScore():
 for name,score in zip(PlayerNameArray,PlayerScoreArray):
  print(f"{name} {score}")


# num > 100 or num < 0
newPlayerName = input("Enter a player name of 3 characters :")
newPlayerScore = int(input("Enter player score between 1 and 100000 inclusive :"))
while (len(newPlayerName) != 3) or (newPlayerScore > 100000 or newPlayerScore < 1) :
    newPlayerName = input("Enter a player name of 3 characters :")
    newPlayerScore = int(input("Enter player score between 1 and 100000 inclusive :"))

newTopTenArrayScores = [0] * 10
newTopTenArrayName = [""] * 10 


def NewTopTen(name,score):
#  print(PlayerScoreArray,PlayerNameArray)
 global newTopTenArrayName
 global newTopTenArrayScores
 PlayerNameArray.append(name)
 PlayerScoreArray.append(score)
 for i in range(len(PlayerScoreArray)-1):
    for j in range((len(PlayerScoreArray)-1)-i):
        if PlayerScoreArray[j] < PlayerScoreArray[j+1]:
            tempScore = PlayerScoreArray[j]
            tempName = PlayerNameArray[j]
            
            PlayerScoreArray[j] = PlayerScoreArray[j+1]
            PlayerNameArray[j] = PlayerNameArray[j+1]
            
            PlayerScoreArray[j+1] = tempScore
            PlayerNameArray[j+1] = tempName
 
 for i in range(10):
   newTopTenArrayName[i] = PlayerNameArray[i]
   newTopTenArrayScores[i] = PlayerScoreArray[i]

 print(PlayerScoreArray,PlayerNameArray)   


def WriteTopTen():
 myFile = open("P4 Booklet Qs/Filling/NewHighScore.txt","w")
 global newTopTenArrayName
 global newTopTenArrayScores
#  for name,score in zip(PlayerNameArray,PlayerScoreArray):
 for index in range(10):
        myFile.write(newTopTenArrayName[index] + "\n")
        myFile.write(str(newTopTenArrayScores[index]) + "\n")

# ReadHighScore()    
# NewTopTen(newPlayerName,newPlayerScore)
# WriteTopTen()
# OutputHighScore()

print(len(PlayerNameArray))