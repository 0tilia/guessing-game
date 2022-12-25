#day 12

from random import randint

#Function to check user's guess against actual answer.


def check_answer(guess, answer):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
  elif guess < answer:
    print("Too low.")
  else:
    print(f"You got it! The answer was {answer}.")


def game():
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 10.")
  answer = randint(1, 10)
  # print(f"Pssst, the correct answer is {answer}")

  #Repeat the guessing functionality if they get it wrong.
  guess = 0

  while guess != answer:
    # print(f"You have {turns} attempts remaining to guess the number.")
    #
    # #Let the user guess a number.
    guess = int(input("Make a guess: "))
    #
    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer)
    # if guess == answer:
    #   print("Correct.")
    #   return
    # elif guess != answer:
    #   print("Guess again.")


game()

