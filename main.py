from os import system
from source.hangman import Hangman


def hangman():
    
    hangman = Hangman()
    
    print('----------------------------------------')

    # Main loop
    while '-' in hangman.word_dashes and hangman.lives > 0:
        
        hangman.draw()
        user_letter = input('\nEnter a letter: ').upper()
        
        system('cls')
        
        hangman.answer(user_letter)
    
    hangman.draw()
    hangman.final_words()
        
        
if __name__ == '__main__':
    hangman()