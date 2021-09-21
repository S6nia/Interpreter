# Name: Sonia Gonçalves
# Program: MSc IT
# ST ID: 13106604
# Date: September 2021


##
# This module defines the MyToken class.
#

INT, PLUS, MINUS, MULT, DIV, LPARENT, RPARENT = (
    'INT', 'PLUS', 'MINUS', 'MULT', 'DIV', 'LPARENT', 'RPARENT'
)

class MyToken:
    '''A MyToken.'''
    
    def __init__(self, desc, value, index):
        '''(MyToken, str, str, int) -> Nonetype

        Initializes the instance variables of token object, given the desc, value and index.

        >>> token = MyToken('INT', '2', 0)
        >>> token.getType()
        'INT'
        >>> token.getValue()
        '2'
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
        'Token {Type: INT, Value: 2, Index: 0}'
        '''

        return 'Token {Type: ' + self._type + ', ' + 'Value: ' + self._value \
               + ', Index: ' + str(self._index) + '}'


    def setValue(self, value):
        '''(MyToken) -> NoneType

        Updates the value of the instance variable self._value.

        >>> token = MyToken('INT', '2', 0)
        >>> token.getValue()
        '2'
        >>> token.setValue('4')
        >>> token.getValue()
        '4'
        '''
        
        self._value = value
    
    
    def getType(self):
        '''(MyToken) -> str

        Return the type of the token (INT, PLUS, MINUS, MULT, DIV, LPARENT, RPARENT).

        >>> token = MyToken('INT', '2', 0)
        >>> token.getType()
        'INT'
        '''
        
        return self._type


    def getValue(self):
        '''(MyToken) -> str

        Return the value of the token.

        >>> token = MyToken('INT', '2', 0)
        >>> token.getValue()
        '2'
        '''
        return self._value


    def getIndex(self):
        '''(MyToken) -> int

        Return the index of the position of the token in the input.

        >>> token = MyToken('INT', '2', 0)
        >>> token.getIndex()
        0
        '''
        
        return self._index


# The following segment is executed if this file is to be run.
if __name__ == '__main__':

    # Testing automatically using doctest module.
    import doctest
    doctest.testmod()

    # Creating some examples:
    tk1 = MyToken(INT, '2', 0)
    tk2 = MyToken(PLUS, '+', 1)

    print(tk1)
    print(tk2)

    
