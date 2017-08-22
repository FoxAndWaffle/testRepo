import os

fruit = ["Apple", "Strawberry", "Banana", "Grapes"]
juice = ["Orange Jiuce", "Apple Juice", "Berry Blast"]
jerky = ["Beef", "Pork", "Turkey", "Duck"]

def clear():
	os.system("cls" if os.name == "nt" else "clear")

def whats_available():
	clear()

	print("Here's what's left...")
	
	for items in fruit:
		print(items)
	for items in jerky:
		print(items)
	for items in juice:
		print(items)

while True:
	choice = input("Would you like FRUIT, JUICE, or JERKY?\n"
					"-> ").lower()

	try:
		if choice == "fruit":
			snack = fruit.pop()
		elif choice == "juice":
			snack = juice.pop()
		elif choice == "jerky":
			snack = jerky.pop()
		elif choice == "done":
			break
		elif choice == "list":
			whats_available()
			continue
		else:
			print("Say...Wuuuut?")
			continue
		print("Here is your {}.".format(snack))
	
	except IndexError:
		print("Sorry, all out of {}.".format(choice))
