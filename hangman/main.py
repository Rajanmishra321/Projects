from hangman_console import stages,logo
from words_list import word_list
import random

game_is_finished=False
lives= len(stages)-1
chosen_word=random.choice(word_list)
display = []
print(chosen_word)

print(logo)

for _ in range(len(chosen_word)):
    display +="_"
print(display)

while not game_is_finished:
    print(f"you have six lives {lives}")
    guess_word=input("enter the word you want to guess :").lower()
    letter_guessed=False
    
        
    for index in range(len(chosen_word)):
        if chosen_word[index]==guess_word:
            if guess_word in display:
                print(f"you already guessed the word {guess_word}, please try something else")
            display[index]=guess_word
            letter_guessed=True
    
        
    if letter_guessed :
            print("goooood you guessed right , “😍” , go ahead ")
            print(display)
            print(stages[lives])
        
    else:
        lives=lives-1
        print("you guessed the worng word ---- you lose a live , “💔” ")
        print(stages[lives])
    
    
    if "".join(display) == chosen_word:
        print('''you won the game ,
              🕺🕺🕺🕺🕺🕺🕺🕺
               👯‍♂️👯‍♂️👯‍♂️👯‍♂️
              🥳🥳🥳🥳🥳🤩🤩🤩🤩''' )
        game_is_finished=True
        
        
    if lives == 0:
        print("you lose the game , better luck next time ")
        game_is_finished=True
   