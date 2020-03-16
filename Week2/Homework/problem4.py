text = input()

print("The given string:", text)
print("The USA/usa count is:", int(str(text).count("USA")) + int(str(text).count("usa")) )
text = text.replace("USA" , "Armenia",int(str(text).count("USA")))
text = text.replace("usa" , "Armenia",int(str(text).count("usa")))

print("The new string:" , text)



