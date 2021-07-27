# Sonia da Trindade
# 24 07 21


# This is an interpreter.
# This is the main file of this program.


# Tokenizer
# Parser
# Evaluator
# Node class
# Test files


def main():

    print("Calculator\nEnter the key 'Q' to exit the program.")
    userInput = input(">>> ")
    while userInput != 'Q':
            
        tokens = tokenize(userInput)
        
        addition = 0
        #for i in range(len(tokens)):
        if tokens[0] == '+':
            for j in range (1, len(tokens)):
                addition += int(tokens[j])
        else:
            print("Other operators are still not defined!")

        print (addition)

        userInput = input(">>> ")

        #parse(tokens)


# What this function does (remember, not how it does!)
def tokenize(userInput):
    '''(str) -> list of strings (tokens)

    Return a list of valid tokens from the string userInput.

    >>> + 1 2
    3
    >>> + 10 20
    30
    >>> + 11 21 31
    63
    '''

    tokens = []
    charList = userInput.split()

    pos = 0
    while pos < len(charList):
        if charList[pos] == '+':
            tokens.append(charList[pos])
        elif charList[pos].isdigit():
            tokens.append(charList[pos])
        else:
            print("Unexpected token!") 
        pos += 1

    return tokens

    
#def parse(tokens):
    

main()
