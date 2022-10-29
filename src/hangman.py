import random
from words import words
import string #for alphabet

def get_valid_word(words):
    word = random.choice(words)

    #keeps iterating until finds a word that has no '-' or ' '
    while '-' in word or ' ' in word: 
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #gets letters from word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user guessed
    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters:', ' '.join(used_letters)) #shows used letters
        word_list = [letter if letter in used_letters else '_' for letter in word] #shows the current word using list comprehensions
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter isn\'t in the word')
        elif user_letter in used_letters:
            print('You have already used that character. Try again!')
        else:
            print('Invalid character. Try again!')

    if lives == 0:
        print(f'Sorry! You died. The word was {word}')
    else:
        print(f'You guessed the word {word}!')

hangman()

