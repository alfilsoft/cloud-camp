def hello_world(lenguaje):
    if(lenguaje=="ENG"):
        print("Hello world".upper())
    elif(lenguaje=="ESP"):
        print("Hola mundo".upper())
        
        
def hello_world2(lenguaje):
    if(lenguaje=="ENG"):
        return "Hello world".upper()
    elif(lenguaje=="ESP"):
        return "Hola mundo".upper()
        
def happy_birthday(name="non_name", age=0):
    print("Happy Birthday "+ str(age) +" "+name)

hello_world("ESP")
hello_world("ENG")

print("Hello world 2")
gretting = hello_world2("ENG")
print(gretting)

happy_birthday("Luis",33)

happy_birthday(age=44,name="Pedro")

happy_birthday()