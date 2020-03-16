print("Enter text:")
text = input()

if len(text) >= 7 and int(len(text)) %2 != 0:
    middle = int(int(len(text)) /2)
    print(middle)
    print(text[ middle -1 : middle + 2 ])
else:
    print("Error!!!")