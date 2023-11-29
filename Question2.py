Color1=input("Enter the Color1")
Color2=input("Enter the color2")


if(Color1=="red",Color1=="yellow",Color1=="blue") :
    print()
else:
    print("Invalid color")


if(Color2=="red",Color2=="yellow",Color2=="blue") :
    print()
else:
    print("Invalid color")
          
if(Color1=="red") :
    if(Color2=="blue"):
        print("Purple")

    if(Color2=="yellow"):
        print("Orange")
elif(Color1=="blue") :
    if(Color2=="red"):
        print("Purple")

    if(Color2=="yellow"):
        print("Orange")

elif(Color1=="yellow") :
    if(Color2=="red"):
        print("Orange")

    if(Color2=="yellow"):
        print("Green")        

