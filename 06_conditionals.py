a = int(input("Enter your age : "))

#  IF ELIF and ELSE ladder in python : 
if(a>=18):
    print("You are above the age of consent ")
    print("Good for you ") 

elif(a<0):
    print("You are entering an Invalid age ")

elif(a ==0 ):
    print("Please specify a correct age ")    

else:
    print("You are below the age of consent ")    

print("End of Program ")