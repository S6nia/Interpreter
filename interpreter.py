# Sonia da Trindade
# 19 08 21

# This is an interpreter. Name: Abacus :)
# This is the main file of this program.

# Main
# Token class
# Tokenizer
# Node class
# Parser
# Evaluator
# Test files for each 

# Documentation: Comments, docstring, preconditions
# Validations and error handling
# Testing (doctest, unittest, assertions)


import tokenizer
import parser
import evaluator

def main():
    '''
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
            
        tk = tokenizer.Tokenizer(userInput)
        tokens = tk.getTokens()
        psr = parser.Parser(tokens) # remember song example
        expression = psr.getExpression()
        eva = evaluator.Evaluator(expression)
        result = eva.getResult()

        print(result)

        userInput = input(">>> ")

    print("The program has exited.")
    

if __name__ == '__main__':
    main()

