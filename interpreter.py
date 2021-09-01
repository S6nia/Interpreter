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

    print("Calculator\nEnter the key 'Q' to exit the program.")
    
    userInput = input(">>> ")
    while userInput.upper() != 'Q':
            
        tk = MyTokenizer(userInput)
        tokens = tk.getListOfTokens()
        psr = MyParser(tokens)
        #expression = psr.getExpression()
        #eva = evaluator.Evaluator(expression)
        #result = eva.getResult()

        result = psr.getResult()

        print(result)

        userInput = input(">>> ")

    print("The program has exited.")
    

if __name__ == '__main__':

    main()

