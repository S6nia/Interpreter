# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 22 08 21


##
# This module defines the MyEvaluator class.
#

import math
from myNode import MyNode

class MyEvaluator:
    '''An evaluator.'''

    # Docstring?
    def __init__(self, node):
        '''(MyEvaluator) -> NoneType'''
        
        self._node = node
        self._result = 0

        
    #def __str__(self):
        

    # Docstring?
    def _performOperation(self):
        '''(MyEvaluator) -> NoneType'''

        if self._node.getRightOperand() == None:

            # Refactor: helper function
            if self._node.getOperator() == '+':
                self._result = (2 * int(self._node.getLeftOperand()))

            elif self._node.getOperator() == '-':
                self._result = (int(self._node.getLeftOperand()) - int(self._node.getLeftOperand()))
                
            elif self._node.getOperator() == '*':
                self._result = math.trunc(math.pow(int(self._node.getLeftOperand()), 2))
                
            else:
                self._result = (int(self._node.getLeftOperand()) / int(self._node.getLeftOperand()))

        else:

            # Refactor: helper function
            if self._node.getOperator() == '+':
                self._result = self._node.getLeftOperand() + self._node.getRightOperand()

            elif self._node.getOperator() == '-':
                self._result = self._node.getLeftOperand() - self._node.getRightOperand()

            elif self._node.getOperator() == '*':
                self._result = self._node.getLeftOperand() * self._node.getRightOperand()

            else:
                self._result = self._node.getLeftOperand() / self._node.getRightOperand()


    # Docstring?
    def getResult(self):
        '''(MyEvaluator) -> int'''

        self._performOperation()

        return self._result


# The following segment is executed if this file is to be run.
if __name__ == '__main__':

    # Testing automatically using doctest module.
    import doctest
    doctest.testmod()
