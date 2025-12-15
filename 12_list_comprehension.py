myList = [1 , 2 , 5 , 7 , 3 , 5 ]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

# Using List Comprehensions :
squaredList = [i*i for i in myList]

print(squaredList)
list1 = [1 , 7 , 12 , 11 , 22 ]
list2 = [item for item in list1 if item > 8 ]
print(list2)
