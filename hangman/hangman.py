import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letter = set()   #what the user has guessed
    life = 6
    #getting user input
    while len(word_letters) > 0 and life > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', life, 'lives left and you have used these letters: ', ' '.join(used_letter))

        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('current word:', ' '.join(word_list) )
        user_letter = input("enter the letter :")

        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if used_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                life = life - 1 #takes life away if you are wrong
        elif user_letter in used_letter:
            print("you already used that letter")
        else:
            print("invalid character ")
    if life == 0:
       
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

hangman()
    


