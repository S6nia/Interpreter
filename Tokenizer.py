# Sonia da Trindade
# 19 08 21


import token

class Tokenizer:
    '''A tokenizer.'''

    def __init__(self, userInput):
        '''(Tokenizer, str) -> NoneType'''

        self._input = userInput # stream of characteres (str)
        self._pos = 0
        self._current_char = self._input[self._pos]
        self._output = [] # stream of lexemes/tokens (list)


    def __str__(self):
        '''(Tokenizer) -> str

        Return a string representation of the tokenizer.

        >>> tk = Tokenizer('+ 1 2')
        >>> str(tk)
        '(+ 1 2) -> Tokenizer -> ['+', '1', '2']'
        '''
        
        return '(' + self._input + ') -> Tokenizer -> ' + self._output
    
    
    def advanceOnePosition(self):
        '''(Tokenizer) -> NoneType '''

        self._pos += 1
        self._current_char = self._input[self._pos]


    # How to write test examples?
    def isMultidigit(self):
        '''(Tokenizer) -> int

        Return a multidigit integer (lexeme). 
        '''
        
        result = 0

        while self._current_char.isdigit():
            result += self._current_char
            self.advanceOnePosition()
            
        return result


    # refactor!
    def prepareDataFromInput(self):
        '''(Tokenizer) -> Token'''

        while self._pos < len(self._input):

            if self._current_char.isspace():
                self.advanceOnePosition()
                continue # this statement returns the control to the beginning of the while loop :)
            
            if self._current_char == '+':
                    tk = token.Token(PLUS, '+', self._pos)
                    self._output.append(tk)
                
            if self._current_char == '-':
                    tk = token.Token(MINUS, '-', self._pos)
                    self._output.append(tk)
                
##            if self._current_char == '*':
##                    self._output.append(Token(MULT, '*', self._pos))
##                
##            if self._current_char == '/':
##                    self._output.append(Token(DIV, '/', self._pos))

            if self._current_char.isdigit():
                    tk = Token(INT, self.IsMultidigit(), self._pos)
                    self._output.append(tk) # need to come up with a better name...
                
            self.advanceOnePosition()
                                       
        # another alterantive for invalid token, e.g. '!'
        # parser verifica de certo modo a ordem dos tokens, eu penso! :)


    def getListOfTokens(self):
        '''(Tokenizer) -> list of Tokens

        Return a list of valid tokens.

        >>> tk = Tokenizer('+ 1 2')
        >>> tk.getListOfTokens()
        ['+', '1', '2']
        '''

        self.prepareDataFromInput()
        
        return self._output


if __name__ == '__main__':

    tkz = Tokenizer('+ 1 2')
    listOfTokens = tkz.getListOfTokens()
    print(listOfTokens)


