from game_data import data
from art import logo, vs
from replit import clear
import random

def get_random_data():
  return random.choice(data)

def format_data(account):
  name = account['name']
  description = account['description']
  country = account['country']
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_follower, b_follower):
  if a_follower > b_follower :
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  score = 0
  game_continue = True
  account_a = get_random_data()
  account_b = get_random_data()

  while game_continue:
    account_a = account_b
    account_b = get_random_data()

    while account_a == account_b:
      account_b = get_random_data()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more follower 'A' or 'B' : ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right, you current score is {score}")
    else:
      game_continue = False
      print(f"You guessed wrong, your final score is {score}")
  while input("Do you want to play again, 'yes' or 'no' :").lower() == "yes":
    clear()
    game()
game()      
    
    
