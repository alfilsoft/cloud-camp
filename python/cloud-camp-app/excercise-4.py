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
        
    def __str__(self):
        return f"{self.name} {self.teacher.name} {len(self.students_list)} {self.teacher.modules}"
        
    def add_student(self,student):
        self.students_list.append(student)
        
pablo = Student("Pab",22,"peru","p.p@e.com")
pedro = Student("Ped",48,"chile","p.elgrande@e.com")
camila= Student("Cam",22,"col","p.labrincona@e.com")
einstein = Teacher("einstein",96,"germany","a.e@e.com")
einstein.setModules(["pytho","bash"])
python_curse= Curse("Python",einstein,[pablo,pedro])
python_curse.add_student(camila)

print(pablo)
print(pedro)
print(einstein)
print(python_curse)
       