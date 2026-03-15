# vowels = ['a','e','i','o','u']

# # for i in range(0,len(vowels)):
# #     print(vowels[i])

# # for item in vowels:
# #     print(item)

# # count = 0
# # while count < 5 :
# #     print(vowels[count])
# #     count += 1

# # if "c" in vowels:
# #     print("true")
# # else:
# #     print("false")


# # for i in range(0,10,2):
# #     print(i)


# # TYPE STUDENTS
#     # DECLARE StudentID : INTEGER
#     # DECLARE Name : STRING

# # DE-CLARE MySTudent : STUDENT
# # MyStudent.Name <- "Mubashir"
# # MyStudent.Name <- "Mubashir"

# # class Student :
# #     # DECLARE PUBLIC StudentID : INTEGER
# #     # DECLARE PUBLIC Name : STRING

# #     def __init__(self,name,studentId):
# #         self.__name = name
# #         self.__StudentID = studentId

# #     def getName(self):
# #         return self.__name    
    
# #     def getStudentID(self):
# #         return self.__StudentID    
    
# #     def setName(self,name):
# #         self.__name = name

# # MyStudent = Student("Mubashir",1182025)
# # MyStudent.setName("Sohaib")

# # print(MyStudent.getName())
# # print(MyStudent.getStudentID())






# # class Student :
# #     # DECLARE PUBLIC Name : STRING
# #     # DECLARE PUBLIC Age : INTEGER

# #     def __init__(self,Pname,Page):
# #         self.name = Pname
# #         self.age = Page
    
# #     def setAge(self):
# #         self.age = self.age + 1
    
# #     def setName(self,Pname):
# #         self.name = Pname

        
# # MyStudent = Student("Mubashir",19)

# # MyStudent.setAge()
# # MyStudent.setName("Abiya")

# # print(MyStudent.age)
# # print(MyStudent.name)


class Student :
    # DECLARE PRIVATE Name : STRING
    # DECLARE PRIVATE Age : INTEGER

    def __init__(self,Pname,Page):  # "Mubashir",19
        self.__name = Pname
        self.__age = Page
    
    # def setAge(self):
    #     self.age = self.age + 1
    
    # def setName(self,Pname):
    #     self.name = Pname

    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age

        
MyStudent = Student("Mubashir",19)

print(MyStudent.getName())

# print(MyStudent.getAge())


class Marks :
    def __init__(self,name,marks) -> None:
        self.name = name
        self.marks = marks

StudentMarks = [Marks('',0) for index in range(3)]

StudentMarks[2] = Marks("Mubashir",40)
StudentMarks[1] = Marks("Tamsila",90)
StudentMarks[0] = Marks('Ali' ,99)

# print(StudentMarks[0].__dict__)

# for index in range(3):
#     if StudentMarks[index].marks > 50 :
#         print(StudentMarks[index].name)

