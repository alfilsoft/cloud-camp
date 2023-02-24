#!/usr/bin/python3

print("Hello welcome to the coffee shop\n")


menu="coffee, tea and wather"
name=input("Hello what's your name\n")
beverage=input("What do you want to drink "+ name +" from the menu "+menu+"\n")

print("your "+beverage+" gonna be ready soon \n")

price=4
units=int(input("how many units you want?  \n"))

max_units=100
if units>max_units:
    print("we just have "+str(max_units)+" unitsgit sta")
else:
    print("the value of your order is: "+str(price*units)+ " USD")
    print(name+ " your "+ beverage + " is going to be ready soon")
