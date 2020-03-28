#1
a1 = ["Cookies" , "Chocolate",8,True,-3,-5, "Chocolate" , 8, False, 8]

#2 
b1 = [8,True,10,14, "Chocolate", "Milk", "Jelly", True , False , True]

#3

set_a = set(a1)
#4
set_b = set(b1)

#5 
union_ab = set_a.union(set_b)
#6
intersection_ab = set_a.intersection(set_b)

#7
union_ab.add("Kit-kat")
union_ab.add("Oreo")


print("Union AB:" , union_ab)

#8

new_set = union_ab or intersection_ab

#9 
print("Chocolate" in new_set)
#10

new_set.discard("Oreo")
print("New set:" , new_set)
