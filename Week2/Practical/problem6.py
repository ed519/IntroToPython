str1 = "How are you John?"
name = "Edgar"
#First method
str2 = str1[:12] + name + "?"
print(str2)


str1 = "How are you John?"
#Second method
str2 = str1.replace("John", name)

print(str2)
