text = input()
digits = len([x for x in text  if x.isdigit()])
print("The given string:", text)
print("Digits:" , digits)
print("Non-digits:", len(text)-digits)
