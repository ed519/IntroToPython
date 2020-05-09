list1 = ['a', 0, 2, True, 'hi']

try:
    print(list1[10])
    
except IndexError:
    print("Index out of range.")

except Exception:
    print("Error.")
