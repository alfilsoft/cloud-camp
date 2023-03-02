
#linux=["Ubuntu","Amazon Linux","Debian","Arch"]

#linux = ("Ubuntu","amazon linux","Debian","Arch")

linux={"Ubuntu":100,"Amazon linux":500,"Debian":1000,"Arch":50}
for server in linux:
    print(server)
    
    if server == "Debian":
        print("I like debian")
        print(linux[server])
        
for letter in "My String":
    print(letter)
    
    