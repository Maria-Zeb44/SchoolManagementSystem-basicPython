from abc import ABC, abstractmethod


class Staff(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary 
    
    def get_salary(self):
        return self.__salary
    
    @abstractmethod
    def role(self):
        pass

class Teacher(Staff):
    def role(self): 
        return f"{self.name} teaches students"

class Admin(Staff):
    def role(self):  
        return f"{self.name} manages office"

class Clerk(Staff):
    def role(self):  
        return f"{self.name} cleans building"


staff = [
    Teacher("abc", 5000),
    Admin("def", 4000),
    Clerk("ghi", 2000)
]

print("Staff Roles and Salaries")
print("=" * 30)
for s in staff:
    print(s.role())
    print(f" Salary: Rs{s.get_salary()}")
    print("-" * 30)