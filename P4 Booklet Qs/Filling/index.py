# # # write mode

# # # myFile = open("Alpha.txt","w")

# # # StudentID = input("Enter Student ID : ")
# # # Name = input("Enter Name : ")
# # # age = input("Enter Age : ")
# # # Gender = input("Enter Gender : ")

# # # info = StudentID + " " + Name + " " + age + " " + Gender

# # # myFile.write(info)
# # # myFile.close()

# # myFile = open("Alpha.txt","a")

# # StudentID = input("Enter Student ID : ")
# # Name = input("Enter Name : ")
# # age = input("Enter Age : ")
# # Gender = input("Enter Gender : ")

# # info = StudentID + " " + Name + " " + age + " " + Gender + "\n"

# # myFile.write(info)
# # myFile.close()


myArray = [0] * 100
# myFile = open("P4 Booklet Qs/Filling/Text Files - P4/Data.txt","r")
# # for index in range(25):
# #     info = int(myFile.readline().strip())
# #     myArray[index] = info

# # print(myArray)
# info = myFile.readline().strip()
# count = 0
# while info != "" :
#     myArray[count] = int(info)
#     count += 1
#     info = myFile.readline().strip()

# print(myArray)



# x = 5
# y = 10
# name = "Mubashir"

# print(x + " " + y + " " + name)

# print(f"Hello {name} age {y}")

# print(name[0])

try:
 myFile = open("P4 Booklet Qs/Filling/Text Files - P4/Data.txt","r") 
 info = myFile.readline().strip()
 count = 0
 while info != "" :
    myArray[count] = int(info)
    count += 1
    info = myFile.readline().strip()

except:
 print("file not found")

print(myArray)