a = int(input("Enter first Number :"))
b = int(input("Enter second Number :"))

if(b == 0 ):
    raise ZeroDivisionError("Hey our Program is not meant to divide Numbers by zero")
else:
    print(f"The Division a/b is {a/b}")
