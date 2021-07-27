# Sonia da Trindade
# 24 07 21

# This is an interpreter.
# This is the main file of this program.

# Tokenizer
# Parser
# Evaluator
# Node class
# Test files

# Comments, docstring
# Validations and error handling


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
            print("Something went wrong!")

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

    # I think it's a good idea to comment every substancial block of code.
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
