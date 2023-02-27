linux=["ubunut","Amazon linux","Debian","arch"]


numeros = ["1",2,"tres",True]
print(linux)

print(numeros)

print(linux[2])

print("list number of elements"+str(len(linux)))

print(linux[len(linux) - 1])

print(linux[-2])

print("debian" in linux)

print("Debian" not in linux)

print(linux.index("Debian"))

print(linux.index("arch"))

linux[1] = "Mx. Linux"

print(linux)

linux.remove("arch")

print(linux)

linux.pop(2)

print(linux)

linux.pop() #delete last element of the list
  
print(linux)

del linux[0] #delete linux var o linux ind
print(linux)

linux.append("new linux")
print(linux)

linux.insert(1,"Mx Linux")
print(linux)

linux.insert(1,"test linux")
print(linux)