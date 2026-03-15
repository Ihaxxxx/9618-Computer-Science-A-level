
# def IterativeVowel(Value):
#     # DECLARE Total,LenghtString : INTEGER
#     # DECLARE FirstCharacter : CHAR
#     Total = 0
#     FirstCharacter = Value[0]
#     print(FirstCharacter)
#     if FirstCharacter == "a" or FirstCharacter == "e" or FirstCharacter == "i" or FirstCharacter == "o" or FirstCharacter == "u" :
#      Total += 1 
#     if len(Value) != 1: 
#         return IterativeVowel(Value[1:])
#     return Total    

# x = IterativeVowel("house")

# print(x)

# # x = "House"
# # print(x[0:5])


x = "Mubashir"
# print(x[0])

# for i in range(len(x)) :
#     print(x[i])


# def IterativeVowels(value):
#     # DECLARE Total,LenghtString : INTEGER
#     # DECLARE FirstCharacter : CHAR

#     Total = 0
#     lengthString = len(value)
#     for x in range(lengthString):
#         print(value)
#         firstCharacter = value[0].lower()
#         # print(firstCharacter)
#         vowels = ['a','e','i','o','u']

#         if firstCharacter in vowels:
#             Total += 1
#         value = value[1:]

# IterativeVowels("MUBASHIR")


# x = "Mubashir"
# print(x[2:len(x)])


def RecursiveIterativeVowels(value):
    if value == "" :
        return 0
    else:
        firstCharacter = value[0].lower()
        # print(firstCharacter)
        vowels = ['a','e','i','o','u']

        if firstCharacter in vowels:
            return 1 + RecursiveIterativeVowels(value[1:])
        else:
            return RecursiveIterativeVowels(value[1:])
        
        

x = RecursiveIterativeVowels("house")
print(x)