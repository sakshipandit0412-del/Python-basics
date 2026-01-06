
class Employee:            
    name = "John"           
    age = 26

emp = Employee()          
type(emp)          
    
print(emp.name)    
print(emp.age)

class Employee:            
    name = "Sana"          
    age = 26

    def hello(self):       
      print("Hello")

emp = Employee()           
emp.hello()   

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def details(self):
        print("Employee Name: ",  self.name)
        print("Employee Age: ", self.age)
 

emp1 = Employee("John", 26)         # creating object named emp1  --> the arguments are passed to init() automatically, and emp1 automatically gets name and age properties as passed
emp2 = Employee("Jane", 24)         # creating object named emp2  --> here also the arguments are passed to inti() without explicit calling

emp1.details()
emp2.details()  