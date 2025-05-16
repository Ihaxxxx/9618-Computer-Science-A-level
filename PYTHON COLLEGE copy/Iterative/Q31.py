
def IterativeVowel(Value):
    # DECLARE Total,LenghtString : INTEGER
    # DECLARE FirstCharacter : CHAR
    FirstCharacter = Value[0]
    print(FirstCharacter)
    if FirstCharacter == "a" or FirstCharacter == "e" or FirstCharacter == "i" or FirstCharacter == "o" or FirstCharacter == "u" :
     Total += 1 
    if len(Value) != 1: 
        return IterativeVowel(Value[1:])
    return Total    

x = IterativeVowel("house")

print(x)

# x = "House"
# print(x[0:5])