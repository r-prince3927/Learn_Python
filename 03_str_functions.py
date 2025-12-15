name ="Harry"
print(len(name))  # length function 
print(name.endswith("ry"))  # endswith function 
print(name.startswith("ha"))  # startswith function 
str = "harry"
count = str.count("r")  # counts the number of letters 
print(count) # Output: 2
capitalized_string = str.capitalize()  # Makes the first letter capital in each word 
                                       # in the given String
print(capitalized_string) # Output: "Harry"
index = str.find("rr")  # finds the letters in the given strings . 
print(index) # Output: 2
replaced_string = str.replace("r", "l")  # replaces the letter in between the Strings . 
print(replaced_string) # Output: "hally"
