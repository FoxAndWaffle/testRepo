import random

# genreate a random number 1 - 10
secret_num = random.randint(1, 10)
guesses = []

def game():
  while len(guesses) < 5:
    try:
     guess = int(input("Guess a number between 1 and 10, inclusive: "))
    except ValueError:
      print("{} isn't a number!".format(guess))
   
    else:
      if guess == secret_num:
        print("Yuuuup, the secret number is {}!".format(guess))
        break
      elif guess > secret_num:
        print("Nope, the secret number is lower than {}.".format(guess))
      else:
        guess < secret_num
        print("Try again, the secret number is higher than {}.".format(guess))
  else:
    print("You didn't get it. The secret number was {}!".format(secret_num))

    play_again = input("Do you want to play again? Y/N?")
    if play_again.lower() != 'n':
      game()
    else:
      prin("See you next time!")

  guesses.append(guess)

  