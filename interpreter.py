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
    print("Please follow the Polish Notation, e.g. '+ 2 3' or '+ 2 (* 1 3)'.")
    print("(Enter the key 'Q' to exit the program)\n")
    
    flag = True

    while flag:

        try:
            # Prompt user for inserting an expression
            userInput = input(">>> ")

        except IOError:
            #print("Could not perform calculations on an empty input.")
            break

        #except ValueError:
            #break

        except ValueError as error:
            print("Error: ", str(error))

        except SyntaxError as error:
            print("Error: ", str(error))

        except ZeroDivisionError as error:
            print("Error: ", str(error))

        except Exception as exceptObj:
            print("Error:", str(exceptObj))

        if not userInput:
            continue

        # Checking the input
        if userInput.upper() != 'Q':

            try:
                # Process input
                tk = MyTokenizer(userInput)
                tokens = tk.getListOfTokens()
                psr = MyParser(tokens)
                result = psr.getResult()
                print(result)

            #except ValueError:
                #break

            except ValueError as error:
                print("Error: ", str(error))
                continue

##            # Process input
##            tk = MyTokenizer(userInput)
##            tokens = tk.getListOfTokens()
##            psr = MyParser(tokens)
##            result = psr.getResult()
##            print(result)

        else:

            # Helper function?
            if userInput.upper() == 'Q':
                userInputExit = input("Are you sure you want to quit the program? Y/N: ")

                if userInputExit.upper() == 'Y':
                    flag = False
                    print("The program has exited.")
                else:
                    print("")
                    print("Welcome back!")
                    

##    flag = True
##
##    while flag:
##
##        try:
##            # Prompt user for inserting an expression
##            userInput = input(">>> ")
##
##            # Checking the input
##            if userInput.upper() != 'Q':
##
##                # Process input
##                tk = MyTokenizer(userInput)
##                tokens = tk.getListOfTokens()
##                psr = MyParser(tokens)
##                result = psr.getResult()
##                print(result)
##
##            else:
##
##                # Helper function?
##                if userInput.upper() == 'Q':
##                    userInputExit = input("Are you sure you want to quit the program? Y/N: ")
##
##                    if userInputExit.upper() == 'Y':
##                        flag = False
##                        print("The program has exited.")
##                    else:
##                        print("")
##                        print("Welcome back!")
##                        #userInput = input(">>> ")
##
##        except EOFError:
##            print("Error: Empty input was unexpected.")


##    userInput = input(">>> ")
##
##    while userInput.upper() != 'Q':
##            
##        tk = MyTokenizer(userInput)
##        tokens = tk.getListOfTokens()
##        psr = MyParser(tokens)
##        result = psr.getResult()
##        print(result)
##
##        userInput = input(">>> ")
##
##        # Helper function?
##        if userInput.upper() == 'Q':
##            userInputExit = input("Are you sure you want to quit the program? Y/N: ")
##
##            if userInputExit.upper() == 'Y':
##                print("The program has exited.")
##            else:
##                print("")
##                print("Welcome back!")
##                userInput = input(">>> ")
                

if __name__ == '__main__':

    main()

