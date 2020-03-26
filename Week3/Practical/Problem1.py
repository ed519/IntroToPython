import sys

list1 = ["hello", 1 , True]

list1.extend(sys.argv[1:])


print(list1)
