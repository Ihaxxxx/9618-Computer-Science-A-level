# # QueueArray = [""]*10

# QueueArray = [0]*10


# print(QueueArray)





# # mylist : int = [[-1,0,-1] for i in range(0,20)]
# # freeNode : int = 0
# # rootpointer : int  = -1

# # def insertion(freenode : int, mylist : list, rootpointer : int):
# #     if freenode <= 19: 
# #         currentpointer : int = rootpointer
# #         data : int = int(input("Enter a number: "))
# #         mylist[freenode][0] = -1
# #         mylist[freenode][1] = data 
# #         mylist[freenode][2] = -1 
# #     if rootpointer == -1: 
# #         rootpointer = 0
# #     else:
# #         placed : bool = False 
# #         while not placed: 
# #             if mylist[freenode][1] > mylist[currentpointer][1]: 
# #                 if


# vowels = ['a','e','i','o','u']
# count = 0
# def vowelCount(data) :
#     global count
#     for val in data :
#         if val.lower() in vowels :
#             count += 1
#     return count
# print(vowelCount("AAA"))

# x = "meow"
# x.lower()


# print(0.1+0.2)





# myfile = open("P4 Booklet Qs/Object Programming/ONLY OOP/TreasureChestData.txt","r")
# Lines = myfile.readlines()
# print(Lines)
# for line in Lines:
#     print(line.strip())

# import random 
# myList = [[0 for _ in range(10)] for _ in range(10)]
# print(myList)

# for row in range(10):
#     for col in range(10):
#         k = random.randint(1,100)
#         myList[row][col] = k

# print(myList)


def factorial(n):
    if n == 1 or n == 0 :
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))