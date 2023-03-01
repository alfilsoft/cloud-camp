class Person:
    def __init__(self,name, age, location, email):
        self.name=name
        self.age=age
        self.location=location
        self.email=email
    
    def __str__(self):
        return f"{self.name} {self.age} {self.location} {self.email}"

class Student(Person):
    pass
   
    
class Teacher(Person):
        
    def setModules(self,modules):
        self.modules=modules
        
class Curse():
    def __init__(self, name, teacher, students_list):
        self.name=name
        self.teacher=teacher
        self.students_list=students_list
        
    def __str__(self)
        return f"{self.name} {self.profesor.n}"
        
pablo = Student("Pab",22,"peru","p.p@e.com")
einstein = Teacher("einstein",96,"germany","a.e@e.com")

print(pablo)
print(einstein)
       