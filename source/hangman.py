from .data import all_words
from .hangman_visual import hangman_animation
from random import choice


class Hangman:
    lives = 7
    
    def __init__(self):
        self.word = choice(all_words)
        self.guess_word = self.word['name'].upper()
        self.hint = self.word['hint'].capitalize()
        self.word_dashes = ['-' for _ in range(len(self.guess_word))]
        self.user_used_letters = []
        self.animation = hangman_animation
    
    def answer(self, user_letter):
        
        if user_letter == 'HELP':
            print('You used this letters: ', ', '.join(self.user_used_letters))
            
        elif user_letter == self.guess_word:
            self.word_dashes = [letter for letter in user_letter]
            
        elif user_letter in self.guess_word:
            for usr_l in user_letter:
                self.word_dashes = [usr_l if usr_l == guess_l else self.word_dashes[idx] for idx, guess_l in enumerate(self.guess_word)]
            
        else:
            print(f"Try anything else. '{user_letter[0]}' is not in the word.\n")
            self.user_used_letters.append(user_letter[0])
            self.lives -= 1
    
    def draw(self):
        
        print(self.animation[self.lives])
        print(f'This word is: {self.hint}\n')
        print(' '.join(self.word_dashes).center(40, ' '))
    
    def final_words(self):
        final_words = 'You win!' if self.lives > 0 else 'You Lose!'
            
        print('\n---------------------------------------\n')
        print(''.join(self.guess_word))
        print(f'\n{final_words}\n')
        print('\n----------------------------------------')
        