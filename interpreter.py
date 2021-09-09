# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 19 08 21


# Code * Create * Write
#   
# Main
# Token
# Tokenizer
# Node
# Parser
# Evaluator
#
# Documentation: Comments, docstring, preconditions, public interfaces (classes)
# Validations, and error handling
# Testing (doctest, unittest, assertions)


##
# This module defines the main function of the program: Interpreter AbaCactus :)
#

from myTokenizer import MyTokenizer
from myParser import MyParser
#import sys
#from termcolor import colored

def main():
    '''
    >>> +1
    2
    >>> +11
    22
    >>> + 1 2
    3
    >>> + 10 20
    30
    '''

    #print(colored("Calculator AbaCactus :)\n", 'green'))
    print("Calculator AbaCactus :)\n")
    print("Please follow the Polish notation, e.g. '+ 2 3' or '+ 2 (* 1 3)'.")
    print("(Enter the key 'Q' to exit the program)\n")
    
    userInput = input(">>> ")

    while userInput.upper() != 'Q':
            
        tk = MyTokenizer(userInput)
        tokens = tk.getListOfTokens()
        psr = MyParser(tokens)
        
        result = psr.getResult()
        result = str(result)
        formattedResult = ''

        # My attempt of inserting commas.
        # Not working?!
        # Helper function?
        #if len(result) < 4:
        #    print(result)
        #    
        #else:
        #    for i in range(0, len(result)):
        #        formattedResult += result[i]
        #        
        #        if i%3 == 0 and i < len(result) - 1:
        #            formattedResult += ','
        #
        #    print(result)

        print(result)

        userInput = input(">>> ")

        # Helper function?
        if userInput.upper() == 'Q':
            userInputExit = input("Are you sure you want to quit the program? Y/N: ")

            if userInputExit.upper() == 'Y':
                print("The program has exited.")
            else:
                print("")
                print("Welcome back!")
                userInput = input(">>> ")


if __name__ == '__main__':

    main()

