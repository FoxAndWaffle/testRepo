#functions.py

def hows_the_parrot():
	print('He\'s pining for the fjords!')

hows_the_parrot()

def lumberjack(name):
	if name.lower() == 'josh':
	    print("josh is a lumberjack and he's ok!")
	else:
		print("{} sleeps all night and {} works all day!".format(name, name))

lumberjack("josh")