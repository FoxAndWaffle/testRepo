import os

# make a list that will hold our items
shopping_list = []

# print out instructions about how to use the app

print("What should we grab at the store?")
print("Enter 'DONE' to quit the app.")


while True:
	
	# ask for new items
	new_item = input("-> ")
	new_item = new_item.lower()

	# quit the app
	if new_item == "done":
		break

	# Type 'Show' to show the list
	elif new_item == "show":
		print("Here is your list")

		for item in shopping_list:
			print(item)

	# Type "Help" to get a little help messege
	elif new_item == "help":
			print("Thanks for using the Listr app. To see you list as it is now type 'Show' then press Enter. To quite the app, type 'Done' then press Enter.")

	# add new items to the list
	shopping_list.append(new_item)


# print out the list

print("Here is your list")

for item in shopping_list:
	print(item)
