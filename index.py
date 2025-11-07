# mylist : int = [[-1,0,-1] for i in range(0,20)]
# freeNode : int = 0
# rootpointer : int  = -1

# def insertion(freenode : int, mylist : list, rootpointer : int):
#     if freenode <= 19: 
#         currentpointer : int = rootpointer
#         data : int = int(input("Enter a number: "))
#         mylist[freenode][0] = -1
#         mylist[freenode][1] = data 
#         mylist[freenode][2] = -1 
#     if rootpointer == -1: 
#         rootpointer = 0
#     else:
#         placed : bool = False 
#         while not placed: 
#             if mylist[freenode][1] > mylist[currentpointer][1]: 
#                 if


vowels = ['a','e','i','o','u']
count = 0
def vowelCount(data) :
    global count
    for val in data :
        if val.lower() in vowels :
            count += 1
    return count
print(vowelCount("AAA"))

x = "meow"
x.lower()