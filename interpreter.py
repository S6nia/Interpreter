# Sonia da Trindade
# 24 07 21

# This is an interpreter.
# This is the main file of this program.

# Main
# Token class
# Tokenizer
# Node class
# Parser
# Evaluator
# Test files for each 

# Documentation: Comments, docstring
# Validations and error handling
# Testing


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
            
        tokens = tokenize(userInput)
        #print(tokens)

        if len(tokens) != 0:
            addition = 0
            if tokens[0] == '+':
                for i in range (1, len(tokens)):
                    addition += int(tokens[i])
            else:
                print("Other operators are still not defined!")

            print(addition)
        else:
            print("Please try again.")

        userInput = input(">>> ")

        #parse(tokens)

    print("The program has exited.")
    

# Comment here what this function does (remember, not how it does!)
def tokenize(userInput):
    '''(str) -> list of strings (tokens)

    Return a list of valid tokens from the string userInput.

    >>> tokenize('+ 1 2')
    ['+', '1', '2']
    >>> tokenize('+ 10 20') 
    ['+', '10', '20']
    >>> tokenize('+ 11 21 31')
    ['+', '11', '21', '31']
    '''

    tokens = []
    charList = userInput.split()

    # Checks the format of the operation - has to take an operator and minimum two arguments
    if len(charList) >= 3:

        # Creats the list of tokens.
        pos = 0
        while pos < len(charList):
            if charList[pos] == '+':
                tokens.append(charList[pos])
            else:
                charList[pos].isdigit()
                tokens.append(charList[pos])
            pos += 1

    else:
        print("Expected format: op arg1 arg2...arg(n). Please use white spaces between the units.")
        

    return tokens

    
#def parse(tokens):
    

main()
