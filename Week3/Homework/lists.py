a = [1,4,5,6,7,-2,0,-1]
#2
print("3th and 5th: " , a[2] , "and" , a[4])

#3
a_sorted = a.copy()
a_sorted.sort(reverse=True)
print("Sorted:" , a_sorted)

#4
print("\n")
print(a_sorted[:2])
print(a_sorted[1:6])

#5
del a_sorted[3]
del a_sorted[2]
#6
print("Sorted:" , a_sorted)

#7

b = ["grapes", "Potatoes" , "tomatoes", "Orange" , "Lemon" , "Broccoli", "Carrot", "Sausages"]

#8
b_sorted = b.copy()
b_sorted.sort(reverse=False)

print("b_sorted:" , b_sorted)

#9
c = a[:3] + b[3:6]     

#10
print("C:" , c )