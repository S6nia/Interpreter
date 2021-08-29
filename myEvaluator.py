# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 22 08 21


##
# This module defines the MyEvaluator class.
#

class MyEvaluator:
    '''An evaluator.'''

    def __init__(self, op, opd1, opd2, order):

        self._operator = op
        self._operand1 = opd1
        self._operand2 = opd2
        self._precedence = order

        self._result = 0

        
    #def __str__(self):
        

    def _performOperation(self):

        if self._operator == '+':
            self._result = self._operand1 + self._operand2

        elif self._operator == '-':
            self._result = self._operand1 - self._operand2

        elif  self._operator == '*':
            self._result = self._operand1 * self._operand2

        else:
            self._result = self._operand1 / self._operand2


    def getResult(self):

        return self._result

        
