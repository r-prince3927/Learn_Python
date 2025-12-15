def goodday(name , ending):
    print("Good Day ! " +name)
    print(ending)
    return "Done"

a = goodday("Harry" , "Thank You")
goodday("Prince" , "Grateful Sir")
goodday("Samir" , "Thanks")
print(a)


#  Default agruments :
def goodDay(name , ending= "Thanks bhaii "):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Harry" , "Thanks")
goodDay("Rohan") # By default uses the default agrument Thanks bhaii



