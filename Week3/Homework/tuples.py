#1
t1 = (1,True, "a" , -2, "Anna")
#2
t1 = t1[:1] + t1[2:]
print("T1=" , t1)

#3
t2 = (1,2,3,4,5)

#4
t3 = t1[:2] + t2[:3]
print("t3=" , t3)

#5
print("t3[2]=" , t3[2])

#6
t4 = [(1,3,5), (8,9), ("Anna", "Bob", "Alice")]
print(t4[0][1])