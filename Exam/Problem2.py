list1 = ['a','b' , 'aabb' , 'edgar']
str1 = input()
str2 = input()
print(list1)
try:
    print(list1.index(str1))
    list1[list1.index(str1)] = str2
    print(list1)
except ValueError:
    print("The value is not in list1.")


