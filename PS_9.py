# Problem  1 :
# f = open ("09_poem.txt")
# content = f.read()
# if("twinkle" in content):
#     print("The word twinkle is present in the content ")
# else :
#     print("The word twinkle is not present in the content ")
# f.close()

# Problem 2 :
# import random
# def game():
#     print("You are playing the game .. ")
#     score = random.randint(1 , 62 )
#     #  Fetch the high score : 
#     with open ("09_Hi-score.txt") as f : 
#         hiscore = f.read()
#         if(hiscore != ""):
#             hiscore = int(hiscore)
#         else :
#             hiscore = 0 


#     print(f"Your Score : {score}")
#     if(score > hiscore ):
#         #  Write this high score to this file . 
#         with open ("09_Hi-score.txt" , "w") as f : 
#             f.write(str(score))
        

#     return score 

# game()

# Problem 3 :
# def generateTable(n):
#     table = ""
#     for i in range (1 , 11):
#         table += f"{n} X {i} = {n*i}\n"

#     with open (f"09_tables/table_{n}.txt" , "w") as f :
#         f.write(table)


# for i in range (2 , 21 ):
#     generateTable(i)

# Problem 4 :
# word = "Donkey"

# with open ("09_file.txt" , "r") as f :
#     content = f.read()

# contentNew = content.replace(word , "######")

# with open ("09_file.txt" , "w") as f :
#     content = f.write(contentNew)


# Problem 5 :
# words = ["Donkey" , "bad" , "dirty" , "ganda"]

# with open ("09_file.txt" , "r") as f :
#     content = f.read()

# for word in words:
#     content = content.replace(word , "#" *len(word))

# with open ("09_file.txt" , "w") as f :
#     content = f.write(content)

# Problem 6 :
# with open ("09_file.txt") as  f :
#     content = f.read()

# if("python" in content):
#     print("Yes python is present")
# else :
#     print("No python is not present")

# Problem 7 :
# with open ("09_file.txt") as  f :
#     lines = f.readlines()
# lineno = 1 
# for line in lines :
#     if("python" in line):
#         print(f"Yes python is present . Line no : {lineno}")
#         break
#     lineno +=1 

# else :
#     print("No python is not present")

# Problem 8 :
# with open ("09_this.txt") as f :
#     content = f.read()

# with open ("09_this_copy.txt" , "w") as f :
#     f.write(content)

# Problem 9 :
# with open ("09_file.txt") as f :
#     content1 = f.read()

# with open ("09_poem.txt") as f :
#     content2 = f.read()

# if(content1 == content2):
#     print("Yes ! these files are identical ")
# else:
#     print("No ! these files are not identical ")    

# Problem 10 :
# with open ("09_this_copy.txt" , "w") as f :
#     f.write("")

# Problem 11 :
# with open ("09_old.txt")as f :
#     content = f.read()

# with open ("09_renamed_by_python.txt" , "w")    as f :
#     f.write(content)
