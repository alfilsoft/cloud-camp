
points_list = [(1,2),(4,5),(7,8)]

uno, dos, tres = points_list
 
for x,y in points_list:
    print("X: "+str(x))
    print("Y: "+str(y))
    
print(uno,dos,tres)

linux2={"Ubuntu":100,"Amazon linux":500,"Debian":1000,"Arch":50}

for server,cantidad in linux2.items():
    print("Server: "+server)
    print("Cantidad: "+ str(cantidad))
    
    
for i in range(10):
    print(i)