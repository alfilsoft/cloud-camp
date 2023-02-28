

cont = 0

while cont<10:
    #print("Hello world")
    
    if(cont%2==0):
       cont +=1
       continue
    
    print(cont)
    cont+=1
    
print("test 1----")
cont=0
while cont<10:
    #print("Hello world")
    
    if(cont%5==0):
       cont +=1
       break
    
    print(str(cont)+"3")
    cont+=1