# Problem 1 : 
'''def greatest(a , b , c ):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b 
    elif(c>a and c>b):
        return c 
a = int(input("Enter 1st Number :"))
b = int(input("Enter 2nd Number :"))
c = int(input("Enter 3rd Number :"))
print(greatest(a , b , c))'''

# Problem 2 :
'''def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Enter temperature in F : "))
c = f_to_c(f)
print(f"{round(c , 2)} °C ")'''

# Problem 3 :
'''print("a")
print("b")
print("c" , end = "")
print("d" , end = "") # The end function prevents the print to print a new line at the end. '''

# Problem 4 :
''' 
sum (1) = 1 
sum (2) = 1 + 2 
sum (3) = 1 + 2 + 3  
sum (4) = 1 + 2 + 3 + 4  
sum (5) = 1 + 2 + 3 + 4 + 5  

sum (n) = 1 + 2 + 3 + 4 + 5 .... n  
sum (n) = sum(n-1) + n 
'''
'''def sum(n):
    if(n ==1):
        return 1 
    return sum(n-1) + n 

print(sum(4))'''

# Problem 5 :
'''def pattern(n):
    if(n == 0):
        return
    print("*" * n )
    pattern(n-1)

pattern(5)'''

# Problem 6 :
'''def inch_to_cm(inch):
    return inch*2.54
n = int(input("Enter value in inches : "))

print(f"The corresponding value in cms is {inch_to_cm(n)}")'''

# Problem 7 :
'''def rem(l , word):
    n =[]
    for item in l :
        if not (item == word):
            n.append(item.strip(word))
    return n 
l = ["Harry" , "Rohan" , "Shubham" , "an"]        

print(rem(l , "an"))'''

# Problem 8 :
'''def table (n):
    for i in range(1 , 11):
        print(f"{n} X {i} = {n*i}")

n = int(input("Enter the number : "))
table(n)'''
