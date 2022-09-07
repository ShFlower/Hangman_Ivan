'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random
from re import A

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried
    
    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    
    def __init__(self, word_list, num_lives=5):
        
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word_list[random.randint(0,num_lives-1)]
        self.list_letters=[]
        self.word_guesses = [len(self.word)]
        self.word_guesses=[] 
        self.word_guesses = ['_'] * len(self.word)
        print(*self.word_guesses)


    def charposition(self,usrLetter) -> list:
        pos = [] #list to store positions for the character entered by user within the word
        for word_index in range(len(self.word)):
            if self.word[word_index] == usrLetter:
               pos.append(word_index)
        return pos
        #alternative way to create pos
        #pos = [i for i,x in enumerate(self.word) if x==usrLetter]
        #return pos
    
    def check_letter(self,usrLetter) -> None:
        if usrLetter in self.list_letters:
            print('You have already attempted this letter, please try another one')
            self.ask_letter
        else:
            self.list_letters.append(usrLetter)
            print(*self.list_letters)
            pos_array = self.charposition(usrLetter)

            #print the occurrence and positions of the usrLetter in word
            #print("no occurences = ")
            #print(len(pos_array))
            #print("at locations ")
            #print(*pos_array)
                
            if len(pos_array) > 0:
                for pos_index in pos_array:
                    print(pos_index)
                    self.word_guesses[pos_index] = usrLetter
                print(*self.word_guesses)
        
    def ask_letter(self):
        while len(self.list_letters) < self.num_lives:
            usrLetter = input('Enter a single character input:  ').lower()        
            if (len(usrLetter)>1 or usrLetter.isalpha()==False):
                print('Please enter just one character as your input:  ')
            
            elif(len(usrLetter)==1 and usrLetter.isalpha()):
                print('That\'s right') 

                # checks if the letter has been entered by user
                # also checks where in the word the letter appears
                self.check_letter(usrLetter)
            else:
                print("Please enter a character as your input: ")
        

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    print("game.word equals : "+ game.word)
    game.ask_letter()


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
