import random

#importing word_list from hangman_words
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages
chosen_word = random.choice(word_list)

end_of_game = False
lives = 6

#Importing the logo from hangman_art.py and print it at the start of the game.

print(logo)

#Creating blanks
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
  
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, printing the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

      #Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}") 
        if letter == guess:
            display[position] = letter

    #Check if user is wrong 
          
    if guess not in chosen_word:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -=1
      print(stages[lives])  
      if lives == 0:
        end_of_game = True
        print("You lose!")
    listToStr = ' '.join(map(str, display))
      
    print(listToStr) 
    if "_" not in display:
      end_of_game = True
      print("You win!")

     
