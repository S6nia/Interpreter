# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 22 08 21


##
# This module defines the MyNode class.
#

class MyNode:
    '''A node.'''

    def __init__(self, operator, leftOpd, rightOpd = None):
        '''(MyNode, str, int, int) -> Nonetype

        Initializes the instance variables of node object, given the operator, leftOpd, rightOpd.

        >>> node = MyNode('+', '1' , '2')
        >>> node.getOperator()
        '+'
        >>> node.getLeftOperand()
        '1'
        >>> node.getRightOperand()
        '2'
        '''

        self._operator = operator
        self._leftOpd = leftOpd
        self._rightOpd = rightOpd        


    def __str__(self):
        '''(MyNode) -> str

        Return a string representation of the node.

        >>> node = MyNode('+', '1', '2')
        >>> str(node)
        'Node {Operator: +, Left value: 1, Right value: 2}'
        '''
        
        if self._rightOpd != None:

            return 'Node {Operator: ' + self._operator + ', ' + 'Left value: ' + str(self._leftOpd) \
                   + ', Right value: ' + str(self._rightOpd) + '}'
        else:
            return 'Node {Operator: ' + self._operator + ', ' + 'Value: ' + str(self._leftOpd) + '}'

        # Improve this for operations involving only one number
        #return 'Node {Operator: ' + self._operator + ', ' + 'Left value: ' + str(self._leftOpd) \
        #      + ', Right value: ' + str(self._rightOpd) + '}'


    def getOperator(self):
        '''(MyNode) -> str

        Return the value of the node (operator).

        >>> node = MyNode('+', '1', '2')
        >>> node.getOperator()
        '+'
        '''
        
        return self._operator


    def getLeftOperand(self):
        '''(MyNode) -> int

        Return the value of the left leaf (left operand).

        >>> node = MyNode('+', '1', '2')
        >>> node.getLeftOperand()
        '1'
        '''
        
        return self._leftOpd


    def getRightOperand(self):
        '''(MyNode) -> int

        Return the value of the right leaf (right operand).

        >>> node = MyNode('+', '1', '2')
        >>> node.getRightOperand()
        '2'
        '''
        
        return self._rightOpd
     

# The following segment is executed if this file is to be run.
if __name__ == '__main__':

    # Testing automatically using doctest module.
    import doctest
    doctest.testmod()

    # Creating some examples:
    # With two leafs
    #node = MyNode('+', 1, 2)

    # With only one leaf
    node = MyNode('+', 2)
    
    print(node)
