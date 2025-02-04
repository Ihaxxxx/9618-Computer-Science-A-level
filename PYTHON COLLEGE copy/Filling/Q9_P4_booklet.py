# DECLARE StackVowel ARAAY OF [1:5] OF STRING
# DECLARE StackConsonant ARAAY OF [1:5] OF STRING
# DECLARE VowelTop , ConsonantTop : INTEGER
StackVowel = [""] * 100
StackConsonant = [""] * 100
ConsonantTop = 0
VowelTop = 0




def PushData(letter):
    global VowelTop
    global ConsonantTop
    if letter in ("a","e","i","o","u"):
        if VowelTop == 100:
            print("Stack Full")
        else:
            StackVowel[VowelTop] = letter    
            VowelTop += 1
    else:   
        if ConsonantTop == 100:
            print("Stack Full")
        else:
            StackConsonant[ConsonantTop] = letter    
            ConsonantTop += 1
            
def ReadData():
    myFile = open("/Users/apple/Documents/A2/COMPUTER SCIENCE/PYTHON COLLEGE/Filling/Text Files - P4/StackData.txt","r")        
    LineInfo = myFile.readline().strip()
    while LineInfo != "":
      PushData(LineInfo)
      LineInfo = myFile.readline().strip()



def PopVowel():
 global VowelTop   
 if VowelTop != 0:
   data = StackVowel[VowelTop-1]
   VowelTop -= 1
   return data  
 else:
    return "No Data"


def PopConsonant():
 global ConsonantTop   
 if ConsonantTop != 0:
   data = StackConsonant[ConsonantTop-1]
   ConsonantTop -= 1
   return data  
 else:
    return "No Data"
 
ReadData()      

DataString = ""

for item in range(0,5):
    UserInput = int(input("Enter 0 for Vowel and 1 for consonant "))
    if UserInput == 0:
        DataString += PopVowel()
    elif UserInput == 1 :
        DataString += PopConsonant()
print(DataString)       
        