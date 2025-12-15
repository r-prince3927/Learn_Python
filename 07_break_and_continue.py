# Break Statement :
for i in range(100):
    if(i==34):
        break # Exit the loop right now 
    print(i)

# Continue Statement:
for i in range(100):
    if(i==34):
        continue # Skip this iteration (34 is skipped)
    print(i)

for i in range(4): 
   print("printing") 
   if(i == 2):   # if i is 2, the iteration is skipped  
         continue 
print(i) 

# Pass statement :
for i in range(645):
    pass # Will not work on this for loop (Does Nothing) 

i = 0
while(i<45):
    print(i)
    i = i+1
