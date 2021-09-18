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
# Validations, and handling exceptions
# Testing (doctest, unittest, assertions)


##
# This module defines the main function of the program: Interpreter AbaCactus :)
#

from myTokenizer import MyTokenizer
from myParser import MyParser
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
    print("Please follow the Polish Notation, e.g. '+ 2 3' or '+ 2 (* 1 3)'.")
    print("(Enter the key 'Q' to exit the program)\n")
    
    flag = True

    while flag:

        try:
            # Prompt the user for inserting an expression
            userInput = input(">>> ")

        except IOError:
            break

        if not userInput:
            continue

        # Check the input
        if userInput.upper() != 'Q':

            try:
                # Process input
                tk = MyTokenizer(userInput)
                tokens = tk.getListOfTokens()
                psr = MyParser(tokens)
                result = psr.getResult()
                print(result)

            except ValueError as error:
                print("Error: ", str(error))
                continue

            except SyntaxError as error:
                print("Error: ", str(error))
                continue

            except ZeroDivisionError as error:
                print("Error: ", str(error))

            except Exception:
                print("Something went wrong.") #Change for 'Invalid expression.' when done with tests.
                continue

        else:
            
            # Helper function?
            # Confirm the will of ending the program or not
            if userInput.upper() == 'Q':
                userInputExit = input("Are you sure you want to quit the program? Y/N: ")

                if userInputExit.upper() == 'Y':
                    flag = False
                    print("The program has exited.")
                else:
                    print("")
                    print("Welcome back!")

                                    
# run this file
if __name__ == '__main__':

    # call main function
    main()

