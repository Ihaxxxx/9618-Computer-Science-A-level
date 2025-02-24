class Employee:
    # DECLARE PRIVATE HourlyPay : REAL
    # DECLARE PRIVATE EmployeeNumber,JobTitle : STRING
    # DECLARE PRIVATE PayYear2022 : ARRA[0:51] OF REAL

    def __init__(self, HourlyPay , EmployeeNumber,JobTitle):
      self.__HourlyPay = HourlyPay
      self.__EmployeeNumber = EmployeeNumber
      self.__JobTitle = JobTitle
      self.__PayYear2022 = [0.0] * 52

    def GetEmployeeNumber(self):
       return self.__EmployeeNumber
    
    def SetPay(self,weekNumber,numberOfHours):
       self.__PayYear2022[weekNumber]  =  numberOfHours * self.__HourlyPay

    def GetTotalPay(self):
      return sum(self.__PayYear2022)
    
    def __str__(self):
        return f"Employee(EmployeeNumber: {self.__EmployeeNumber}, HourlyPay: {self.__HourlyPay}, JobTitle: {self.__JobTitle} , HoursWorked : {self.__PayYear2022[0]}  )"


class Manager(Employee):
    # DECLARE PRIVATE BonusValue : REAL
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, BonusValue):
       super().__init__(HourlyPay, EmployeeNumber, JobTitle)
       self.__bonusValue = BonusValue

    def SetPay(self,weekNumber,numberOfHours):
       adjusted_hours = numberOfHours * (1 + self.__bonusValue / 100)
       super().SetPay(weekNumber, adjusted_hours)
    def __str__(self):
        return f"Manager(EmployeeNumber: {self.GetEmployeeNumber()}, HourlyPay: {self._Employee__HourlyPay}, JobTitle: {self._Employee__JobTitle}, BonusValue: {self.__bonusValue} , HoursWorked : {self._Employee__PayYear2022[0]})"   

EmployeeArray = []

myFile = open('PYTHON COLLEGE copy/Object Programming/ONLY OOP/Employees.txt', 'r')
linesArray = myFile.readlines()


count = 0
index = 0
while index < len(linesArray):
   hourlyPay = float(linesArray[index].strip())
   employeeNumber = linesArray[index+1].strip()
   nextVal = linesArray[index+2].strip()[0].lower()
   if 'a' <= nextVal <= 'z':
     JobTittle = linesArray[index+2].strip()
     EmployeeArray.append(Employee(hourlyPay,employeeNumber,JobTittle))
     index += 3
   else:
     bonusVal = float(linesArray[index+2].strip())
     JobTittle = linesArray[index+3].strip()
     EmployeeArray.append(Manager(hourlyPay,employeeNumber,JobTittle,bonusVal))
     index += 4


def EnterHours():
   global EmployeeArray
   HoursWorkFile = open("PYTHON COLLEGE copy/Object Programming/ONLY OOP/HoursWeek1.txt",'r')
   count = 0 
   while count < 8 : 
    employeeNumber = HoursWorkFile.readline().strip()
    hoursWorked = float(HoursWorkFile.readline().strip())                                                                                                                                      
    for index in range(8):
       if EmployeeArray[index].GetEmployeeNumber() == employeeNumber:
          EmployeeArray[index].SetPay(0,hoursWorked)
    count += 1         

EnterHours()

for emp in EmployeeArray:
    print(emp)