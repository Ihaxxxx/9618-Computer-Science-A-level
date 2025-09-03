class Students:
    # PRIVATE StudentID : STRING
    # PRIVATE Name : STRING
    # PRIVATE Age : INTEGER
    # PRIVATE Gender : CHAR
    
    # Constructor
    def __init__(self):
      self.__StudentID = ""  
      self.__Name = ""
      self.__Age = 0
      self.__Gender = ""
      self.__StudentID = ""  
      self.__Name = ""
      self.__Age = 0
      self.__Gender = ""
      
    # Setter  
    def SetID(self,ID):
       self.__StudentID = ID
    
    def SetName(self,Name):
     self.__Name = Name 
     
    def SetAge(self,Age):
     self.__Age = Age 
     
    def SetGender(self,Gender):
     self.__Gender = Gender 
     
    # Getter
    
    def GetID(self):
     return self.__StudentID 
 
    def GetName(self):
     return self.__Name 

    def GetAge(self):
     return self.__Age  

    def GetGender(self):
     return self.__Gender  

    def DisplayDetails(self):
        print("Student ID: ",self.__StudentID )
        print("Gender: ",self.__Gender )
        print("Name: ",self.__Name )
        print("Age: ",self.__Age )
        
class Subjects(Students):
    # PRIVATE Subject1 : INTEGER 
    # PRIVATE Subject1 : INTEGER
    # PRIVATE Subject1 : INTEGER
    
    def __init__(self):
        super().__init__()
        self.__Subject1 = 0
        self.__Subject2 = 0
        self.__Subject3 = 0

    def SetSubjects(self,s1,s2,s3):
     self.__Subject1 = s1
     self.__Subject2 = s2
     self.__Subject3 = s3
    
    def isplayDetails(self):
        Students.DisplayDetails(self)
        # super().DisplayDetails()
        print("1st Subject:  ",self.__Subject1)
        print("2nd Subject:  ",self.__Subject2)
        print("3rd Subject:  ",self.__Subject3)
    
    
# add one data for studenrs
# myStudent = Students()

# myStudent.SetID("100")
# myStudent.SetName("poly")
# myStudent.SetAge("9")
# myStudent.SetGender("M")
# myStudent.DisplayDetails()

# add multiple data for students 

# myList = [Students() for index in range(0,3)]

# for index in range(0,3):
#  id = input("Enter Your ID     : ")
#  name = input("Enter Your Name   : ")
#  age = int(input("Enter Your Age    : "))
#  gender = input("Enter Your Gender : ").capitalize()
 
#  myList[index].SetID(id)
#  myList[index].SetName(name)
#  myList[index].SetAge(age)
#  myList[index].SetGender(gender)

# displat data for students in an array
# for index in range(0,3):
#     myList[index].DisplayDetails()



# add single data for subjetcs

# myStudent = Subjects()
# myStudent.SetID("100")
# myStudent.SetName("poly")
# myStudent.SetAge("9")
# myStudent.SetGender("M")
# myStudent.setSubjects(9618,9702,9231)
# myStudent.displayDetails()



myList = [Subjects() for index in range(0,3)]

for index in range(0,3):
 id = input("Enter Your ID     : ")
 name = input("Enter Your Name   : ")
 age = int(input("Enter Your Age    : "))
 gender = input("Enter Your Gender : ").capitalize()
 sub1 = int(input("Enter your first Subject : "))
 sub2 = int(input("Enter your second Subject : "))
 sub3 = int(input("Enter your third Subject : "))
 
 myList[index].SetID(id)
 myList[index].SetName(name)
 myList[index].SetAge(age)
 myList[index].SetGender(gender)
 myList[index].SetSubjects(sub1,sub2,sub3)

# displat data for students in an array
for index in range(0,3):
    myList[index].DisplayDetails()