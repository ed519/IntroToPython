
list5 = [1,2,3,4,3,2,12,3,4,32,34,123]
print("List:" , list5)
new_list = list5.copy()

del new_list[0]
del new_list[4]
del new_list[5]

print("New_list:" , new_list)
