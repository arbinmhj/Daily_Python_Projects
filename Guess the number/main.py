from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, turns):#function to check the answer guessed by the user
  if guess > answer :
    print("Your guess is high.")
    return turns - 1
  elif guess < answer :
    print("Your guess is low.")
    return turns - 1
  else:
    print(f"You guessed the right number, it's {answer}")
  

def set_difficulty():#setting the difficulty level inputted by user
  level = input("Choose your desired level, type 'hard' or 'easy' : ")
  if level == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL
def play_game():
  print(logo)
  print("Welcome to the number guessing game")
  print("I'm thinking of a number between 1 and 100")
  answer = randint(1, 100)
  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts left to guess the answer")
    guess = int(input("Guess the number : "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You ran out of lives, you lose!!")
      return
    elif guess != answer:
      print("Guess again.")
play_game()      
