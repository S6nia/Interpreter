# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 22 08 21


##
# This module defines the MyNode class.
#


#INT, PLUS, MINUS, MULT, DIV = 'INT', 'PLUS', 'MINUS', 'MULT', 'DIV'

# I still don't know what to do with this, but I'am having this intuition...
##ROOT, PARENT, CHILD, LEAF, RLEAF, LNODE, RNODE, DEPTH  = (
##    'ROOT', 'PARENT', 'CHILD', 'LEAF', 'RLEAF', 'LNODE', 'RNODE', 'DEPTH'
##)

#ROOT, LNODE, RNODE, LEAF, RLEAF = 'ROOT', 'LNODE', 'RNODE', 'LEAF', 'RLEAF'

OPERATOR, LOPERAND, ROPERAND = 'OPERATOR', 'LOPERAND', 'ROPERAND'

class MyNode:
    '''A node.'''

    def __init__(self, operator, leftOpd, rightOpd = None):
        '''(MyNode, str, int, int) -> Nonetype

        >>> node = MyNode('ROOT', '+' , 2)
        >>> node.getType()
        'ROOT'
        >>> node.getValue()
        '+'
        >>> node.getPosition()
        2
        '''

        self._operator = operator
        self._leftOpd = leftOpd
        self._rightOpd = rightOpd
        

##        def __init__(self, desc, value, pos):
##        '''(MyNode, str, str, int) -> Nonetype
##
##        >>> node = MyNode('ROOT', '+' , 2)
##        >>> node.getType()
##        'ROOT'
##        >>> node.getValue()
##        '+'
##        >>> node.getPosition()
##        2
##        '''
##
##        self._type = desc
##        self._value = value
##        self._pos = pos



    def __str__(self):
        '''(MyNode) -> str

        Return a string representation of the node.

        >>> node = MyNode('ROOT', '+', 2)
        >>> str(node)
        'Node {type: ROOT, value: +, position: 2}'
        '''

##        return 'Node {type: ' + self._type + ', ' + 'value: ' + self._value \
##               + ', position: ' + str(self._pos) + '}'

        return 'Node {operator: ' + self._op + ', ' + 'leftValue: ' + str(self._op1) \
               + ', rightValue: ' + str(self._op2) + '}'


    def getOperator(self):
        '''(MyNode) -> str

        Return the type of the node.

        >>> node = MyNode('ROOT', '+', 2)
        >>> node.getType()
        'ROOT'
        '''
        
        return self._operator


    def getLeftOperand(self):
        '''(MyNode) -> str

        Return the value of the node.

        >>> node = MyNode('ROOT', '+', 2)
        >>> node.getValue()
        '+'
        '''
        return self._leftOpd


    def getRightOperand(self):
        '''(MyNode) -> int

        Return the index of the position of the node in the list of nodes.

        >>> node = MyNode('ROOT', '+', 2)
        >>> node.getPosition()
        2
        '''
        
        return self._rightOpd
     

# The following segment is executed if this file is to be run.
if __name__ == '__main__':

    # Testing automatically using doctest module.
##    import doctest
##    doctest.testmod()

    # Creating some examples
    # Taking as an example: + (* 2 3) (* 3 3)
##    node1 = MyNode('LEAF', '3', 0)
##    node2 = MyNode('RLEAF', '3', 1)
##    node3 = MyNode('LEAF', '2', 2)
##    node4 = MyNode('RLEAF', '3', 3)
##    node5 = MyNode('LNODE', '*', 4)
##    node6 = MyNode('RNODE', '*', 5)
##    node7 = MyNode('ROOT', '+', 6)
##
##    nodes = [node1, node2, node3, node4, node5, node6, node7]
##    
##    for node in nodes:
##        print(node)


    #node1 = MyNode('+', 2, 2)
    node1 = MyNode('+', 2)
    print(node1)
