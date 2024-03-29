# Name: Sonia Gonçalves
# Program: MSc IT
# ST ID: 13106604
# Date: September 2021


##
# This module defines the MyEvaluator class.
#

import math
from myNode import MyNode


class MyEvaluator:
    '''A MyEvaluator.'''

    def __init__(self, node):
        '''(MyEvaluator) -> NoneType'''
        
        self._node = node
        self._result = 0


    def __str__(self):
        '''(MyEvaluator) -> str

        Return a string representation of the parser.

        >>> node = MyNode('+', 1, 2)
        >>> eva = MyEvaluator(node)
        >>> result = eva.getResult()
        >>> print(eva)
        (+ 1 2) = 3
        '''

        if self._node.getRightOperand() != None:
            return '(' + self._node.getOperator() + ' ' + str(self._node.getLeftOperand()) + ' ' + \
                   str(self._node.getRightOperand()) + ') = ' + str(self._result)

        else:
            return '(' + self._node.getOperator() + ' ' + str(self._node.getLeftOperand()) + ') = ' + \
                   str(self._result)
        

    def _performOperation(self):
        '''(MyEvaluator) -> NoneType'''

        # Evaluates expressions with only one operand.
        if self._node.getRightOperand() == None:

            # Refactor
            if self._node.getOperator() == '+':
                self._result = (2 * int(self._node.getLeftOperand()))

            elif self._node.getOperator() == '-':
                self._result = (int(self._node.getLeftOperand()) - int(self._node.getLeftOperand()))
                
            elif self._node.getOperator() == '*':
                self._result = math.trunc(math.pow(int(self._node.getLeftOperand()), 2))
                
            else:
                if int(self._node.getLeftOperand()) != 0:
                    self._result = (int(self._node.getLeftOperand()) / int(self._node.getLeftOperand()))
                else:
                    raise ZeroDivisionError("Zero division error ocurred.")
                
        # Evaluates expressions with two operands.      
        else:

            # Refactor
            if self._node.getOperator() == '+':
                self._result = self._node.getLeftOperand() + self._node.getRightOperand()

            elif self._node.getOperator() == '-':
                self._result = self._node.getLeftOperand() - self._node.getRightOperand()

            elif self._node.getOperator() == '*':
                self._result = self._node.getLeftOperand() * self._node.getRightOperand()

            else:

                if self._node.getRightOperand() != 0:
                    self._result = self._node.getLeftOperand() / self._node.getRightOperand()
                else:
                    raise ZeroDivisionError("Zero division error ocurred.")


    def getResult(self):
        '''(MyEvaluator) -> int

        Return the result of the evaluation of the expression.

        >>> node = MyNode('+', 1, 2)
        >>> eva = MyEvaluator(node)
        >>> result = eva.getResult()
        >>> print(result)
        3
        '''
        
        self._performOperation()

        return self._result


# The following segment is executed if this file is to be run.
if __name__ == '__main__':

    # Testing automatically using doctest module.
    import doctest
    doctest.testmod()

    # Creating some examples:
    #node = MyNode('+', 11)
    node = MyNode('+', 1, 2)
    
    eva = MyEvaluator(node)
    result = eva.getResult()
    print(result)

    print(eva)

