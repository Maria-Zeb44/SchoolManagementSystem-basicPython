from abc import ABC, abstractmethod
#task 1
class Staff(ABC):
    def __init__(self, name, salary):
        self.name = name #encapsulation
        self.__salary = salary 
    
    def get_salary(self):
        return self.__salary
    
    @abstractmethod # abstraction
    def role(self):
        pass

class Teacher(Staff):
    def role(self): #polymorphism
        return f"{self.name} teaches students"

class Admin(Staff):
    def role(self):  
        return f"{self.name} manages office"

class Clerk(Staff):
    def role(self):  
        return f"{self.name} cleans building"

school_staff = [
    Teacher("abc", 5000),
    Admin("def", 4000),
    Clerk("ghi", 2000)
]

print("Staff Roles and Salaries")
print("=" * 30)
for s in school_staff:
    print(s.role()) #inheritance
    print(f" Salary: Rs{s.get_salary()}")
    
