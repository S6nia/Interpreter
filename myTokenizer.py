# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 19 08 21


##
# This module defines the MyTokenizer class.
#

from myToken import MyToken

INT, PLUS, MINUS, MULT, DIV, LPARENT, RPARENT = (
    'INT', 'PLUS', 'MINUS', 'MULT', 'DIV', 'LPARENT', 'RPARENT'
)

class MyTokenizer:
    '''A tokenizer.'''

    # Docstring?
    def __init__(self, userInput):
        '''(MyTokenizer, str) -> NoneType'''

        self._input = userInput # Input: stream of chars (str)
        self._pos = 0
        self._currentChar = self._input[self._pos]
        self._output = [] # Output: stream of lexemes/tokens (list of str)


    def __str__(self):
        '''(MyTokenizer) -> str

        Return a string representation of the tokenizer.

        >>> tkz = MyTokenizer('+ 1 2')
        >>> tokens = tkz.getListOfTokens()
        >>> print(tkz)
        '+ 1 2' -> Tokenizer -> ['+', '1', '2']
        '''

        lst = []
        for tk in self._output:
            lst.append(tk.getValue())
        
        return '\'' + self._input + '\' -> Tokenizer -> ' + str(lst)
    

    # Docstring?
    def _creaTokens(self):
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

                elif self._currentChar == '(':
                    tk = MyToken(LPARENT, '(', self._pos)
                    self._output.append(tk)

                elif self._currentChar == ')':
                    tk = MyToken(RPARENT, ')', self._pos)
                    self._output.append(tk)

                elif self._currentChar.isdigit():

                    if not self._input[self._pos - 1].isdigit():
                        tk = MyToken(INT, self._currentChar, self._pos)
                        self._output.append(tk)
                        
                    else:
                        value = self._output[-1].getValue() + self._currentChar
                        self._output[-1].setValue(value)

                else:
                    # needs to be improved based on the info attached to the char.
                    # to give more info to the user.
                    print("Invalid character in the position: ", self._pos)
                                                


    def getListOfTokens(self):
        '''(Tokenizer) -> list of Tokens

        Return a list of valid tokens.

        >>> tkz = MyTokenizer('+ 1 2')
        >>> tokens = tkz.getListOfTokens()
        >>> print(tkz)
        '+ 1 2' -> Tokenizer -> ['+', '1', '2']
        '''

        self._creaTokens()
        
        return self._output


# The following segment is executed if this file is to be run.
if __name__ == '__main__':

    # Testing automatically using doctest module.
    import doctest
    doctest.testmod()

    # Creating some examples:
    # Testing whitespaces
    #tkz = MyTokenizer('+ 1 2')
    #tkz = MyTokenizer('+ 1  2')
    #tkz = MyTokenizer(' + 1 2')
    #tkz = MyTokenizer('+ 1 2 ')
    #tkz = MyTokenizer('+1 2')
    #tkz = MyTokenizer('+12')

    # Testing with other operators
    #tkz = MyTokenizer('- 1 2')
    #tkz = MyTokenizer('* 1 2')
    #tkz = MyTokenizer('/ 1 2')
    #tkz = MyTokenizer('+ 1 2 3')

    # Testing with multi-digit integers
    #tkz = MyTokenizer('+ 11 22 ')
    #tkz = MyTokenizer('+11 22 ')
    #tkz = MyTokenizer('* 3 111')
    #tkz = MyTokenizer(' +12')

    # Testing invalid token
    #tkz = MyTokenizer(' !12')
    #tkz = MyTokenizer(' 12!')

    # Testing valid token, but invalid grammar(parser job)
    #tkz = MyTokenizer(' 12+')

    # Testing with parentheses
    #tkz = MyTokenizer('+ (* 2 3) (* 2 4)')

    # Testing with nested parentheses
    tkz = MyTokenizer('+ (* 2 3) (* (* 2 1) (* 2 2))')
    tokens = tkz.getListOfTokens()

    for tk in tokens:
        print(tk)
        print()

    print(tkz)

