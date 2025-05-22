# DECLARE FirstEmpty,FirstNode : INTEGER
# DECALRE LinkedList  ARRAY [[0:1],[0,19]] OF INTEGER   

FirstEmpty = 0
FirstNode = -1
LinkedList = [[0 for i in range(2)] for x in range(20)]


for index in range(19):
    LinkedList[index][0] = -1
    LinkedList[index][1] = index + 1
LinkedList[19][0] = -1
LinkedList[19][1] = -1



def InsertData():
    global LinkedList,FirstEmpty,FirstNode
    for i in range(5) :
        if FirstEmpty != -1 :
        #     currentNode = FirstEmpty
        #     nextPosition = LinkedList[FirstEmpty][1]
        #     LinkedList[currentNode][1] = FirstNode
        #     LinkedList[currentNode][0] = int(input("Enter a value : "))
        #     FirstEmpty = currentNode
        #     FirstNode = nextPosition
        # else :
        #     print("List is full")    
            nextEmpty = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = int(input("Value: "))
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = nextEmpty
        else:
            print("list is full")            

def OutputLinkedList() :
    global FirstNode,LinkedList
    currentNode = FirstNode
    while currentNode != -1 :
        print(LinkedList[currentNode][0])
        currentNode = LinkedList[currentNode][1]


def RemoveData(item) :
    empytList = 0
    global FirstNode,LinkedList,FirstEmpty
    currentPointer = FirstNode
    previousPointer = -1
    found = False
    while currentPointer != -1 and not found:
        if LinkedList[currentPointer][0] == item:
            found = True
            if previousPointer == -1 :
                FirstNode = LinkedList[currentPointer][1]
            else:
                LinkedList[previousPointer][1] = LinkedList[currentPointer][1]

            LinkedList[currentPointer][1] = FirstEmpty
            FirstEmpty = currentPointer
        else:
            previousPointer = currentPointer
            currentPointer = LinkedList[currentPointer][1]                        

                


InsertData()
RemoveData(5)
print("After")
OutputLinkedList()