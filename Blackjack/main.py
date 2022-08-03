import random
from art import logo
from replit import clear
should_continue = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
  your_card = random.choice(cards)
              #random.sample(cards, 2) to import two random values at once from the list
  return your_card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
  
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return"You went over, you lose!"

  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0 :
    return"You lose, Opponent has blackjack."
  elif user_score == 0 :
    return "You win, you have a blackjack."
  elif user_score > 21:
    return"You went over, you lose!"
  elif computer_score > 21:
    return"Opponent went over, you win!"
  elif user_score > computer_score : 
    return "You win with a high number!"
  else:
    return "You lose!"

def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  game_over = False

  for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21 :
      game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass :")
      if user_should_deal == "y":
        user_cards.append(deal_cards())
      else :
        game_over = True

    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_cards())
      computer_score = calculate_score(computer_cards)
      
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()