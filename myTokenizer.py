# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 19 08 21


##
# This module defines the Tokenizer class.
#

from myToken import MyToken

INT, PLUS, MINUS, MULT, DIV, LPAREN, RPARENT = (
    'INT', 'PLUS', 'MINUS', 'MULT', 'DIV', 'LPAREN', 'RPARENT'
)

class MyTokenizer:
    '''A tokenizer.'''

    def __init__(self, userInput):
        '''(MyTokenizer, str) -> NoneType'''

        self._input = userInput # stream of chars (str)
        self._pos = 0
        self._currentChar = self._input[self._pos]
        self._output = [] # stream of lexemes/tokens (list)


    def __str__(self):
        '''(MyTokenizer) -> str

        Return a string representation of the tokenizer.

        >>> tkz = MyTokenizer('+ 1 2')
        >>> print(tkz)
        '(+ 1 2) -> Tokenizer -> ['+', '1', '2']'
        '''

        lst = []
        for tk in self._output:
            lst.append(tk.getValue())
        
        return '(' + self._input + ') -> Tokenizer -> ' + str(lst)

    
    def _prepareDataFromInput(self):
        '''(Tokenizer) -> NoneType'''

        for self._pos in range(len(self._input)):

            self._currentChar = self._input[self._pos]

            if self._currentChar.isspace():
               continue # this statement returns the control to the beginning of the while loop :) 

            else:

                if self._currentChar == '+':
                    tk = MyToken(PLUS, '+', self._pos)
                    self._output.append(tk)
                
                elif self._currentChar == '-':
                    tk = MyToken(MINUS, '-', self._pos)
                    self._output.append(tk)

                elif self._currentChar == '*':
                    tk = MyToken(MULT, '*', self._pos)
                    self._output.append(tk)

                elif self._currentChar == '/':
                    tk = MyToken(DIV, '/', self._pos)
                    self._output.append(tk)

                elif self._currentChar.isdigit():
                    tk = MyToken(INT, self._currentChar, self._pos)
                    self._output.append(tk)

                else:
                    print("Invalid character!") # needs to be improved based on the info attached to the char.
                                                # to give more info to the user.


    def getListOfTokens(self):
        '''(Tokenizer) -> list of Tokens

        Return a list of valid tokens.

        >>> tkz = Tokenizer('+ 1 2')
        >>> tokens = tkz.getListOfTokens()
        >>> ... ... ... ... ... ... ... ...
        >>> print(list((tokens[0].getValue()), tokens[1].getValue()), tokens[2].getValue())))
        ['+', '1', '2']
        '''

        self._prepareDataFromInput()
        
        return self._output


if __name__ == '__main__':

    #import doctest
    #doctest.testmod()

    # Creating some examples
    #tkz = MyTokenizer('+ 1 2')
    #tkz = MyTokenizer('+ 1  2')
    #tkz = MyTokenizer(' + 1 2')
    #tkz = MyTokenizer('+ 1 2 ')
    #tkz = MyTokenizer('+1 2')
    #tkz = MyTokenizer('+12')

    # Tests with other operators:
    #tkz = MyTokenizer('- 1 2')
    #tkz = MyTokenizer('* 1 2')
    #tkz = MyTokenizer('/ 1 2')
    tkz = MyTokenizer('+ 1 2 3')
    
    print(tkz)
    #print(tkz._currentChar)
    #print(tkz._pos)
    print()
    
    tokens = tkz.getListOfTokens()
    #print(tokens[0])
    #print(list((tokens[0].getValue(), tokens[1].getValue(), tokens[2].getValue())))

    for tk in tokens:
        print(tk)
        print(tk._type)
        print(tk._value)
        print(tk._index)
        print()

    print(tkz)

