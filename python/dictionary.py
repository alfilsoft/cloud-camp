#dictionary

inventory={"Ubuntu":100,"Amazon linux":500,"Debian":1000,"Arch":50}

print(inventory)
print(inventory["Debian"])
print(inventory["Arch"])

print(inventory.get("debian")) #get method does not trhow any exception
#print(inventory["debian"])

inventory["Debian"]=232
print(inventory.get("Debian"))

inventory["test"]=22

print(inventory)

inventory.pop("test") #remove element from dictionary

print(inventory)

print(inventory.keys())
print(list(inventory.keys()))

print(inventory.values())