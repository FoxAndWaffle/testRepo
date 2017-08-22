import os

# make a list that will hold our items
shopping_list = []

def clear():
	os.system("cls" if os.name == "nt" else "clear")

def show_help():
	clear()
	# print out instructions about how to use the app
	print("Thanks for using the Listr app.\n"
		"Enter 'Show' to see your list.\n"
		"Enter 'Help' for instructions.\n"
		"Enter 'Done' to quit.\n"
		"Enter 'Remove' to remove an item")

def show_list():
	clear()
	
	print("Here is your list")
	
	index = 1
	for item in shopping_list:
		print("{}. {}".format(index, item))
		index += 1

	print("-"*10)

# add new items to the list
def add_items(new_item):
	show_list()
	if len(shopping_list):
		position = input("Where should I add {}?\n"
						"Press Enter to add to the end of the list.\n"
						"->".format(new_item))
	else:
		position = 0

	try:
		position = abs(int(position))
	except ValueError:
		position = None
	if position is not None:
		shopping_list.insert(position-1, new_item)
	else:
		shopping_list.append(new_item)

	show_list()



# remove all instances of an item
def remove_item():
	clear()
	show_list()
	thing = input("What would you like to remove?\n->")

	try:
		shopping_list.remove(thing)
	except ValueError:
		pass
	show_list()


while True:
	
	# ask for new items
	new_item = input("-> ")
	new_item = new_item.lower()

	# quit the app
	if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
		break
	# Show help
	elif new_item.upper() == "HELP":
		show_help()
		continue
	# show help
	elif new_item.upper() == "SHOW":
		show_list()
		continue
	# remove item
	elif new_item.upper() == "REMOVE":
		remove_item()

	else:
		add_items(new_item)

show_list()

# print out the list
print("Here is your list")

for item in shopping_list:
	print(item)
