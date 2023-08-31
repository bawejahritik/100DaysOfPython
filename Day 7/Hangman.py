import random
import Hangman_words

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)

word_list = ["ardvark", "baboon", "camel"]

word = random.choice(Hangman_words.word_list)
user_word = ["_"] * len(word)
words_input = []
lives_left = 6

while '_' in user_word and lives_left>0:
    user_input = input("Guess a letter: ").lower()
    lose_life = True
    for i in range(len(word)):
        if user_input in words_input:
            print("Already Used!")
            lose_life=False
            break
        elif user_input==word[i]:
            user_word[i] = user_input
            lose_life = False
    words_input.append(user_input)
    
    if lose_life:
        lives_left -= 1
    

    print(user_word)
    if lives_left<6:
        print(stages[lives_left])


if lives_left>0:
    print("You Win!")
else:
    print(f"Psst! The word was {word}")