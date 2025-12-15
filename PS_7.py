# Problem 1 :
'''n = int(input("Enter a number : ") )
for i in range(1 , 11 ):
    print(f"{n} X {i} = {n * i}")'''

# Problem 2 :
'''l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l :
    if(name.startswith("S")):
        print(f"Hello {name}")'''

# Problem 3 :
'''n = int(input("Enter a number "))
i = 1 
while(i < 11 ):
    print(f"{n} X {i} = { n * i }")
    i = i+1 '''

# Problem 4 :
'''n = int(input("Enter a Number :"))

for i in range(2 , n ):
    if((n%i)==0):
        print("It is not a Prime Number ")
        break
else:
    print("It is a Prime Number ")'''

# Problem 5 :
'''n = int(input("Enter a Number :"))
i = 1
sum = 0 
while(i<=n):
    sum +=i
    i+=1 

print(sum)'''

# Problem 6 :
# Farctorial : 5! = 1 X 2 X 3 X 4 X 5 
'''n = int(input("Enter a Number :"))
product = 1 
for i in range(1 , n +1 ):
    product = product * i 

print(f"The factoraial of {n} is {product}")'''

# Problem 7 :
''' for n = 3 
  *
 ***
*****    
'''
'''n = int(input("Enter a Number :"))
for i in range(1 , n+1):
    print(" " * (n-i), end = "") 
    print("*" * (2*i-1), end = "")
    print("")'''

# Problem 8 :
'''n = int(input("Enter a Number :"))
for i in range(1 , n+1):
    print("*" * i, end = "")
    print("")'''

# Problem 9 :
''' n = int(input("Enter a Number :"))
for i in range(1 , n+1):
    if(i == 1 or i == n ):
        print("*"*n , end="")
    else:
        print("*" , end= "")
        print(" " * (n-2), end= "")
        print("*" , end= "")
    print("")'''

# Problem 10 :
'''n = int(input("Enter a Number : "))

for i in range(1 , 11 ):
    print(f"{n} X {11-i} = {n * (11-i)}")'''
