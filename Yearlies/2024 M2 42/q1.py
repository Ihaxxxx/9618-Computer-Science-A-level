WordArray = []
answerCount = 0
correctCount = 0

def ReadWords(filename):
    global WordArray,answerCount
    myFile  = open(filename + ".txt","r")  
    info = myFile.readline().strip()
    while info != "" :
        WordArray.append(info)
        info = myFile.readline().strip()
    answerCount = len(WordArray)-1 
    Play()


ans = input("Enter which level you want to play 'easy' , 'medium' or 'hard' ").capitalize()


ReadWords(ans)
# print(WordArray,answerCount)


def Play():
    global WordArray,answerCount,correctCount
    print("The main word is " + WordArray[0] + " the number of correct answers are " + str(answerCount))

    userAns = input("Enter a word which you think is ans : ")

    while userAns != "no" :
        if userAns in WordArray :
            correctCount += 1 
            index = WordArray.index(userAns)
            WordArray[index] = None
            userAns = input("correct wanna try again if not press enter no if yes enter another guess: ")
        else : 
            userAns = input("wrong wanna try again if not press enter no if yes enter another guess: ")
    print("The percentage of answers user entered correct are " + str(correctCount/answerCount * 100))    
    for index in range(1,len(WordArray)):
        if WordArray[index] != None:
            print(WordArray[index])

