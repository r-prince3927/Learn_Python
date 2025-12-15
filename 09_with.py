f = open("09_file.txt")

print(f.read())
f.close()

# The same can be written using with statement like this : 
with open ("09_file.txt") as f :
    print(f.read())
#  File closes automatically . 
# You don't have to close the file explicitly . 

