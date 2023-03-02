#cloud camp management

#student
pablo = {"name":"Pablo P","age":22,"location":"Peru","email":"pablo@cloud.com"}
pedro = {"name":"Pedro care chimba","age":25,"location":"Colombia","email":"pedro@cloud.com"}

#teacher
einstein = {"name":"Albert Einstein","age":30,"location":"Germany","email":"albert@cloud.com","modulos":["bash","python"]}

print(einstein)

def courseCreation(teacher, list_of_students, topic):
    return {"teacher":teacher,"students":list_of_students, "topic":topic}

curso = courseCreation(einstein,[pedro,pablo],"Bash")

print(curso)

print(curso.get("teacher").get("name"))

for student in curso.get("students"):
    print(student.get("name"))



