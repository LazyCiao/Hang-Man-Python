import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words) # random word from list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word as a set
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # user guesses

    guesses = 10

    # User input
    while len(word_letters) > 0 and guesses > 0:
        print('You have', guesses, 'guesses left and you have used these letters: ', ' '.join(used_letters))

        world_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(world_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                guesses = guesses - 1
                print('\n', user_letter, 'is not in the word. Try again.')

        elif user_letter in used_letters:
            print('\nYou have already used that character. Try again.')
        
        else:
            print('\n', user_letter, 'is not a valid character, try again')  

    if guesses == 0:
        print('You died, sorry. the word was', word)
    else:
        print('You Guessed the word', word, 'correctly')

if __name__=='__main__':
    hangman()