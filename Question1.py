a=int(input("Enter the Day"))
b=int(input("Enter the Month"))
c=int(input("Enter the Year"))

if(a>31):
  print("Invalid Day Input")
if (b>12):
  print("Invalid Month Input") 
if(c>99):
 print("Invalid Year Input")                   

if(b==2):
  if(c%4==0 and a>29):
     print("Invalid  date") 

  if(c%4!=0 and a>28):
     print("Invalid  date") 

print(a,"/",b,"/",c)