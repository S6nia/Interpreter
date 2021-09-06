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
# This module defines the main function of the program: Interpreter Abacus :)
#

from myTokenizer import MyTokenizer
from myParser import MyParser
#from myEvaluator import MyEvaluator
#import sys
#from termcolor import colored

def main():
    '''
    >>> 1
    1
    >>> + 1 2
    3
    >>> + 10 20
    30
    >>> + 11 21 31
    63
    '''

    #print(colored("Calculator AbaCactus :)\n", 'green'))
    print("Calculator AbaCactus :)\n")
    print("Please follow the Polish notation, e.g. '+ 2 3' or '+ 2 (* 1 3)'.")
    print("(Enter the key 'Q' to exit the program)\n")
    
    userInput = input(">>> ")

    if userInput.upper() != 'Q':
    
        while userInput.upper() != 'Q':
            
            tk = MyTokenizer(userInput)
            tokens = tk.getListOfTokens()
            psr = MyParser(tokens)
            #expression = psr.getExpression()
            #eva = evaluator.Evaluator(expression)
            #result = eva.getResult()

            result = psr.getResult()
            print(result)

##          node = psr.getNode()
##          eva = evaluator.Evaluator(node)
##          result = eva.getResult()
##          #result = str(eva)
##
##          print(result)
##          #print(eva)

            userInput = input(">>> ")

            if userInput.upper() == 'Q':
                userInputExit = input("Are you sure you want to quit the program? Y/N: ")

                if userInputExit.upper() == 'Y':
                    print("The program has exited.")
                else:
                    userInput = input(">>> ")


##    userInput = input(">>> ")
##    
##    while userInput.upper() != 'Q':
##            
##        tk = MyTokenizer(userInput)
##        tokens = tk.getListOfTokens()
##        psr = MyParser(tokens)
##        #expression = psr.getExpression()
##        #eva = evaluator.Evaluator(expression)
##        #result = eva.getResult()
##
##        result = psr.getResult()
##        print(result)
##
####        node = psr.getNode()
####        eva = evaluator.Evaluator(node)
####        result = eva.getResult()
####        #result = str(eva)
####
####        print(result)
####        #print(eva)
##
##        userInput = input(">>> ")
##    
##    print("The program has exited.")
    

if __name__ == '__main__':

    main()

