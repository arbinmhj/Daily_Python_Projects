import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)
else :
  print('Invalid input, please try again!')

length = len(list)
random_choice = random.randint(0, length-1)
computer_choice = list[random_choice]
print(f"Computer choice:\n\n {computer_choice}")

if user_choice == 0 and random_choice == 2:
  print("You win!")
elif random_choice > user_choice :
  print("You lose!")
elif user_choice > random_choice :
  print("You win!")
elif random_choice == user_choice:
  print("Tie!")
else:
  print("Invalid!")

  


