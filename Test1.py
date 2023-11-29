a=int(input("Enter the Day"))
b=int(input("Enter the Month"))
c=int(input("Enter the Year"))

if(a>31):
  print("Invalid Day")
if (b>12):
  print("Invalid Month") 
if(c>99):
 print("Invalid Year")                   

if(b==2):

   if(c%4==0):
   
      if(a>29):
             print("Invalid  Day")   
  