# write mode

# myFile = open("Alpha.txt","w")

# StudentID = input("Enter Student ID : ")
# Name = input("Enter Name : ")
# age = input("Enter Age : ")
# Gender = input("Enter Gender : ")

# info = StudentID + " " + Name + " " + age + " " + Gender

# myFile.write(info)
# myFile.close()

myFile = open("Alpha.txt","a")

StudentID = input("Enter Student ID : ")
Name = input("Enter Name : ")
age = input("Enter Age : ")
Gender = input("Enter Gender : ")

info = StudentID + " " + Name + " " + age + " " + Gender + "\n"

myFile.write(info)
myFile.close()
