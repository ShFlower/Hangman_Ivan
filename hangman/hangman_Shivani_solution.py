'''
Code written by Shivani Flower
Date 05 Septemebr 2022

Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, dont add any more prints
or you will get 0 for this assignment.
'''
import random
from turtle import end_fill

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
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # 2. {word_guessed}

        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word_list[random.randint(0,num_lives-1)]
        self.list_letters=[]
        self.word_guesses = [len(self.word)]
        #self.word_guesses=[] 
        self.word_guesses = ["_"] * len(self.word)
        print('*******************************************************************')
        print(f'Mystery Word : {self.word_guesses}')
        print(f'You have : {self.num_lives} lives')
        print('*******************************************************************')

    def charposition(self,usrLetter) -> list:
        pos = [] #list to store positions for the character entered by user within the word
        for word_index in range(len(self.word)):
            if self.word[word_index] == usrLetter:
               pos.append(word_index)
        return pos
        
        #alternative way to create pos
        #pos = [i for i,x in enumerate(self.word) if x==usrLetter]
        #return pos

    def check_letter(self, usrLetter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked
             '''
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A word can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        

        if usrLetter in self.list_letters: #check if letter already tried
            print('You have already tried this letter, please try another one')
            
        else: #if letter not already tried add to list
            self.list_letters.append(usrLetter)
            pos_array = self.charposition(usrLetter) #find positions in mystery word where letter occurs
                       
            if len(pos_array) > 0: #if letter found in Mystery word populate word_guesses on each occurence                for pos_index in pos_array:
                for pos_index in pos_array:
                    self.word_guesses[pos_index] = usrLetter

            else:
                print('The letter was not found!')
                self.num_lives -= 1 #decrement number of lives if not a previously guessed letter
                
            # display to user latest status on letters guessed, mystery word known and num_lives       
            print(f'Letters you have guessed so far : {self.list_letters}')
            print(f'Mystery Word : {self.word_guesses}')
            print(f'You still have : {self.num_lives} lives')   

       

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method

        # loop while there are unguessed letters in mystery word or the user has lives left  
        while bool({"_"} & set(self.word_guesses)) or (self.num_lives > 0):

            #if all letters in mystery word have been guessed then display user message and exit program
            if bool({"_"} & set(self.word_guesses)) == False:
                print('')
                print('********************************************************************************')
                print('')
                print(f'You have guessed the Mystery Word : {self.word_guesses} with {self.num_lives} lives left') 
                print('')
                print('********************************************************************************')
                exit()

            elif (self.num_lives == 0):
                print('')
                print('********************************************************************************')
                print('')
                print(f'You have run out of lives. The Mystery Word is : {self.word}') 
                print('')
                print('********************************************************************************')
                exit()
            
            else: #otherwise keep looping the game               
                print('') # user dipaly formatting
                print('----------------------------------------------------------------')  # user dipaly formatting
                usrLetter = input('Enter a single character input:  ').lower()        
                if (len(usrLetter)>1 or usrLetter.isalpha()==False):
                    print('Please enter just one character as your input:  ')

                elif(len(usrLetter)==1 and usrLetter.isalpha()):
                    print('That\'s right') 
                    self.check_letter(usrLetter)  # checks if the letter has been entered by user where in the word the letter appears
                
                else:
                    print("Please enter a character as your input: ")
        
def play_game(word_list):
    # As an aid, part of the code is already provided:
    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"

    game = Hangman(word_list, num_lives=5)
    
    game.ask_letter()

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
