# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 18 08 21


##
# This module defines the Token class.
#

INT, PLUS, MINUS, MULT, DIV, LPAREN, RPARENT = (
    'INT', 'PLUS', 'MINUS', 'MULT', 'DIV', 'LPAREN', 'RPARENT'
)

class MyToken:
    '''A token.'''
    
    def __init__(self, desc, value, index):
        '''(MyToken, str, str, int) -> Nonetype

        >>> token = MyToken('INT', 2, 0)
        >>> token.getType()
        'INT'
        >>> token.getValue()
        2
        >>> token.getIndex()
        0
        '''

        self._type = desc
        self._value = value
        self._index = index
        
    
    def __str__(self):
        '''(MyToken) -> str

        Return a string representation of the token.

        >>> token = MyToken('INT', '2', 0)
        >>> str(token)
        'Token {type: INT, value: 2, index: 0}'
        '''

        return 'Token {type: ' + self._type + ', ' + 'value: ' + self._value \
               + ', index: ' + str(self._index) + '}'

    
    def getType(self):
        '''(MyToken) -> str

        Return the type of the token (INT, PLUS, MINUS, MULT, DIV, LPAREN, RPAREN).

        >>> token = MyToken('INT', 2, 0)
        >>> token.getType()
        'INT'
        '''
        
        return self._type


    def getValue(self):
        '''(MyToken) -> str

        Return the value of the token.

        >>> token = MyToken('INT', 2, 0)
        >>> token.getValue()
        2
        '''
        return self._value


    def getIndex(self):
        '''(MyToken) -> int

        Return the index of the position of the token in the input.

        >>> token = MyToken('INT', 2, 0)
        >>> token.getIndex()
        0
        '''
        
        return self._index


# The following segment is executed if this file is to be run.
if __name__ == '__main__':

    # Testing automatically using doctest module.
    import doctest
    doctest.testmod()

    # Creating some examples.
    tk1 = MyToken(INT, '2', 0)
    tk2 = MyToken(PLUS, '+', 1)

    print(tk1)
    print(tk2)

    print(tk1._type)
    print(tk2._type)
    print(tk1.getType())
    print(tk2.getType())
    print(tk1.getValue())
    print(tk2.getValue())
    print(tk1.getIndex())
    print(tk2.getIndex())
    
  
