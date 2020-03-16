import sys
print("Enter the text:")
text = input()

first_word = sys.argv[1]
second_word = sys.argv[2]

print("The given text:", text)
print("First word:", first_word)
print("Second word:", second_word) 
print("Output string:", str(text).replace(first_word, second_word) )

