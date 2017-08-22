import os
import sys
import random

# make a list of words
word_list = [
	"cat",
	"dog",
	"bat"
]

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

# draw guessed letters and strikes
def draw(bad_guess, good_guess, secret_word):
	clear()
	print('Strikes: {}/7'.format(len(bad_guess)))
	print('')
	for letter in bad_guess:
		print(letter, end=' ')
	print('\n\n')
	for letter in secret_word:
		if letter in good_guess:
			print(letter, end='')
		else:
			print('_', end='')
	print('')

# take a guess
def get_guess(bad_guess, good_guess):
	while True:
		guess = input("Guess a letter: ").lower()
		if len(guess) != 1:
			print("You can only guess one at a time.")
		elif guess in bad_guess or guess in good_guess:
			print("You've already guessed that letter.")
		elif not guess.isalpha():
			print("You can only guess letters.")
		else:
			return guess

def play(done):
	clear()
	# pick a random word from the list and store the guesses
	secret_word = random.choice(word_list)
	bad_guess = []
	good_guess = []

	while True:
		draw(bad_guess, good_guess, secret_word)
		guess = get_guess(bad_guess, good_guess)

		if guess in secret_word:
			good_guess.append(guess)
			found = True
			for letter in secret_word:
				if letter not in good_guess:
					found = False
			if found:
				print("You win!")
				print("The correct word is {}".format(secret_word))
				done = True
		else:
			bad_guess.append(guess)
			if len(bad_guess) == 7:
				draw(bad_guess, good_guess, secret_word)
				print("You loose!")
				print("The secret word was {}.".format(secret_word))
				done = True
		
		if done:
			play_again = input("Platy again? Y/n").lower()
			if play_again != 'n':
				return play(done=False)
			else:
				sys.exit()

def welcome():
	start = input("Wlecome to the game. Press 'Q' to quit. Otherwise, press Enter.").lower()
	if start == 'q':
		print('Bye! :-)')
		sys.exit()
	else:
		return True

print("Wlecome to the Letter Game!")

done = False

while True:
	clear()
	welcome()
	play(done)


	# pull from list of woeds in database
	# guess the whole word
	# number of guesses changes based on the word length
	






