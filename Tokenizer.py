# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 19 08 21


##
# This module defines the Tokenizer class.
#

import token

class Tokenizer:
    '''A tokenizer.'''

    def __init__(self, userInput):
        '''(Tokenizer, str) -> NoneType'''

        self._input = userInput # stream of chars (str)
        self._pos = 0
        self._currentChar = self._input[self._pos]
        self._output = [] # stream of lexemes/tokens (list)


    def __str__(self):
        '''(Tokenizer) -> str

        Return a string representation of the tokenizer.

        >>> tkz = Tokenizer('+ 1 2')
        >>> print(tkz)
        '(+ 1 2) -> Tokenizer -> ['+', '1', '2']'
        '''
        
        return '(' + self._input + ') -> Tokenizer -> ' + self._output


    def advanceByOne(self):
        '''(Tokenizer) -> NoneType'''

        self._pos += 1
        self._currentChar = self._input[self._pos]
    

    def getMultidigitInteger(self):
        '''(Tokenizer) -> int

        Return a multidigit integer (lexeme). 
        '''
        
        result = ''

        while self._currentChar.isdigit():
            result += self._currentChar
            self.advanceByOne()
            
        return result

    
    def prepareDataFromInput(self):
        '''(Tokenizer) -> NoneType'''

        while self._pos < len(self._input):

            if self._currentChar.isspace():
                self.advanceByOne()
                continue # this statement returns the control to the beginning of the while loop :) 
            
            else:

                if self._current_char == '+':
                    tk = token.Token(PLUS, '+', self._pos)
                    self._output.append(tk)
                
                elif self._current_char == '-':
                    tk = token.Token(MINUS, '-', self._pos)
                    self._output.append(tk)

                elif self._current_char == '*':
                    tk = token.Token(MULT, '*', self._pos)
                    self._output.append(tk)

                elif self._current_char == '/':
                    tk = token.Token(DIV, '/', self._pos)
                    self._output.append(tk)

                elif self._current_char.isdigit():
                    tk = token.Token(INT, self.getMultidigitInteger(), self._pos)
                    self._output.append(tk) # need to come up with a better name...

                else:
                    print("Invalid character!") # needs to be improved based on the info attached to the char.
                                                # to give more info to the user.
                
            self.advanceByOne()


    def getListOfTokens(self):
        '''(Tokenizer) -> list of Tokens

        Return a list of valid tokens.

        >>> tkz = Tokenizer('+ 1 2')
        >>> tokens = tkz.getListOfTokens()
        >>> print(tokens)
        ['+', '1', '2']
        '''

        self.prepareDataFromInput()
        
        return self._output


if __name__ == '__main__':

    #import doctest
    #doctest.testmod()

    tkz = Tokenizer('+ 1 2')
    Tokens = tkz.getListOfTokens()
    print(Tokens)

