class EventItem:
    # DECLARE EventName,Type : STRING
    # DECLARE Difficulty : INTEGER 

    def __init__(self,EventName,Type,Difficulty):
        self.__EventName = EventName
        self.__Type = Type
        self.__Difficulty = Difficulty

    def GetName(self):
        return self.__EventName
    
    def GetDifficulty(self):
        return self.__Difficulty
    
    def GetType(self):
        return self.__Type
    

class Character():
    # DECLARE CharacterName : STRING
    # DECLARE Jump,Swim,Run,Drive : INTEGER
    def __init__(self,CharacterName,Jump,Swim,Run,Drive):
        self.__CharacterName = CharacterName
        self.__Jump = Jump
        self.__Swim = Swim
        self.__Run = Run
        self.__Drive = Drive

    def GetName(self):
        return self.__CharacterName

    def CalculateScore(self,EventType,Difficulty):
        value = 0 
        if EventType == "jump":
            value = self.__Jump
        elif EventType == "swim":
            value = self.__Swim
        elif EventType == "run":
            value = self.__Run
        elif EventType == "drive":
            value = self.__Drive

        if value >= Difficulty:
            return 100
        
        difference = Difficulty - value
        if difference < 0 :
            difference = -1 * difference

        if difference == 1 :
            return 80
        elif difference == 2 :
            return 60
        elif difference == 3 :
            return 40
        elif difference == 4 :
            return 20


Group = []
Group.append(EventItem("Bridge","jump",3))
Group.append(EventItem("Water wade","swim",4))
Group.append(EventItem("100 mile run","run",5))
Group.append(EventItem("Gridlock","drive",2))
Group.append(EventItem("Wall on wall","jump",4))



Tarz = Character("Tarz",5,3,5,1)
Geni = Character("Geni",2,2,3,4)


tarzScore = 0
GeniScore = 0
for index in range(5):
    # print(Group[index].GetDifficulty())
    tarzChance = Tarz.CalculateScore(Group[index].GetType(),Group[index].GetDifficulty())
    print(tarzChance)
    GeniChance = Geni.CalculateScore(Group[index].GetType(),Group[index].GetDifficulty())
    print(GeniChance)
    if tarzChance > GeniChance :
        print(f"Tarz has a better chance of winning the event {Group[index].GetName()} so he gets a point")
        tarzScore += 1
    if tarzChance < GeniChance :
        print(f"Geni has a better chance of winning the event {Group[index].GetName()} so he gets a point")
        GeniScore += 1
    elif tarzChance == GeniChance:
        print(f"Both Tarz and Geni have an equal chance of winning {Group[index].GetName()} so no one won it  ")


if tarzScore > GeniScore :
    print(f"Tarz has a better chance of winning the Group with a score of {tarzScore}")
if tarzScore < GeniScore :
    print(f"Geni has a better chance of winning the Group with a score of {GeniScore}")
elif tarzScore == GeniScore:
    print("Both Tarz and Geni have an equal chance of winning the event so no one won it  ")














