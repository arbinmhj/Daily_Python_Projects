from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The highest bidder is {winner} with a bid of ${highest_bid}")
    
while not bidding_finished:
  name = input("Enter your name:" )
  amount = int(input("Enter your bid amount: $"))
  bids[name] = amount
  should_continue = input("Are there anymore bidders, type 'yes' or 'no'\n")
  if should_continue == "yes":
    clear()
  elif should_continue == "no":
    bidding_finished = True
    print("The bidding has finished")
    highest_bidder(bids)
