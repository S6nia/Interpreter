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

    def __init__(self, node):

        self._node = node
        self._result = 0

        
    #def __str__(self):
        

    def _performOperation(self):


        if self._node.getRightOperand() == None:

            #helper function for one single number
            if self._node.getOperator() == '+':
                self._result = (2 * int(self._node.getLeftOperand()))

            elif self._node.getOperator() == '-':
                self._result = (int(self._node.getLeftOperand()) - int(self._node.getLeftOperand()))
                
            elif self._node.getOperator() == '*':
                self._result = math.trunc(math.pow(int(self._node.getLeftOperand()), 2))
                
            else:
                self._result = (int(self._node.getLeftOperand()) / int(self._node.getLeftOperand()))

        else:
            
            if self._node.getOperator() == '+':
                self._result = self._node.getLeftOperand() + self._node.getRightOperand()
                #print(self._result)

            elif self._node.getOperator() == '-':
                self._result = self._node.getLeftOperand() - self._node.getRightOperand()

            elif self._node.getOperator() == '*':
                self._result = self._node.getLeftOperand() * self._node.getRightOperand()

            else:
                self._result = self._node.getLeftOperand() / self._node.getRightOperand()


    def getResult(self):

        self._performOperation()

        return self._result

        
