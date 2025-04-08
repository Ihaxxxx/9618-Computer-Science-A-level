class Character:
    # DECLARE CharacterName : STRING
    # DECLARE DateOfBirth : DATE
    # DECLARE Intelligence : REAL
    # DECLARE Speed : INTEGER
    
    def __init__(self,CharName,DOB,Intelligence,Speed):
        self.CharacterName = CharName
        self.DateOfBirth = DOB
        self.Intelligence = Intelligence
        self.Speed = Speed
    
    def GetIntelligence(self):
        return self.Intelligence    
    
    def GetName(self):
        return self.CharacterName
    
    def SetIntelligence(self,intelli):
        self.Intelligence = intelli
    
    def Learn(self):
        self.Intelligence = float(self.Intelligence) *  1.1
        
    def GetAge(self):
     return 2023 - int(self.DateOfBirth.split()[-1])

class MagicCharacter(Character):
    # DECLARE Element : STRING
    def __init__(self, CharName, DOB, Intelligence, Speed,Element):
        super().__init__(CharName, DOB, Intelligence, Speed)
        self.Element = Element
        
    def Learn(self):
        if self.Element == "fire" or self.Element == "water":
          self.Intelligence = float(self.Intelligence) *  1.2
        elif  self.Element == "earth":
            self.Intelligence = float(self.Intelligence) *  1.3
        else:
            self.Intelligence = float(self.Intelligence) *  1.1    
            


FirstCharacter = Character("Royal","1 January 2019","70","30")

FirstCharacter.Learn()

print(f"{FirstCharacter.GetName()} is {FirstCharacter.GetAge()} years old and has an intelligence of {FirstCharacter.GetIntelligence()} and a speed of {FirstCharacter.Speed}")


FirstMagic = MagicCharacter("Light","3 March 2018",75,22,"fire")
FirstMagic.Learn()

print(f"{FirstMagic.GetName()} is {FirstMagic.GetAge()} years old and has an intelligence of {FirstMagic.GetIntelligence()} and a speed of {FirstMagic.Speed} and has an element {FirstMagic.Element}")
