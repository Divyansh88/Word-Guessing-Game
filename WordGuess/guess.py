import sys

from stringDatabase import *
from game import *

class guess:
    '''
    This class provides menu to the user and interact with the user.
    '''

    current_guess = "----"
    current_word = ""

    @classmethod
    def wordSelect(cls):
        '''
        This method takes a new word from stringDatabase class.
        '''
        stringDatabase.lettersToList()
        cls.current_word = stringDatabase.word()
        cls.current_guess = "----"
        print(cls.current_word)         ############# Do not forget to comment.

    @classmethod
    def userMenu(cls):
        '''
        This method will print user menu and ask for user response and do accordingly.
        '''
        print("----------------- The great guessing game -----------------\n")
        print("Current guess:  ", cls.current_guess)

        choice = input("""
g = guess, t = tell me, l for a letter, and q to quit

Enter your choice:
""")
        if choice == 'g':
            value = gm.guessWord(cls.current_word, cls.current_guess)
            if value:
                print("You guessed correct!!!")
                guess.wordSelect()
            else:
                print("Your guess is wrong!!! Sorry!!!")
            guess.userMenu()

        elif choice == 't':
            value = gm.tellAnswer(cls.current_word, cls.current_guess)
            print("Your word is '", value, "'.")
            guess.wordSelect()
            guess.userMenu()

        elif choice == 'l':
            value_compare = cls.current_guess
            value = gm.guessLetter(cls.current_word, cls.current_guess)
            if value_compare==value:
                print("Your guess is wrong!!! Try again!!!")
            else:
                print("Awesome!!! You guessed it right.")
                cls.current_guess = value
            if cls.current_guess==cls.current_word:
                print("Wonderful!!! You guessed the word!!!")
                guess.wordSelect()
            guess.userMenu()

        elif choice == "q":
            print("Thank you, See you again!!!")
            gm.printScore()
            sys.exit(0)

        else:
            print("Enter correct option.")
            guess.userMenu()

    def main(self):
        '''
        This method is main method and it will call other methods.
        '''
        guess.wordSelect()
        guess.userMenu()

if __name__ == "__main__":
    g = guess()
    gm = game()
    g.main()
