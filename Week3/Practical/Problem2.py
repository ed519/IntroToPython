import sys

list1 = ["hello", 1 , True]
new_list = list1.copy()
new_list.extend(sys.argv[1:])

print(list1)
print(new_list)


