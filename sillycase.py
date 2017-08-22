def sillycase(word):
	half = len(word)//2
	new = word[:half].lower() + word[half:].upper()

print(new)


