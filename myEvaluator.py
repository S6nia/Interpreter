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

        stringResult = str(self._result)
        newStr = ''
        
        if len(stringResult) < 4:
            return self._result

        else:
            #i = 0
            #while i < len(stringResult):
                
            for i in range(0, len(stringResult)):
                #newStr = stringResult[i]
                newStr += stringResult[i]

                if i % 3 == 0 and i < len(stringResult) - 1:
                    newStr = newStr + ','
                        
##                    for j in range(i):
##                        newStr = stringResult[i]
##                    newStr
##                    
##                    #while i < len(stringResult):
##                        #for j in range(i+1,i+3):
##                     
##                            newStr = stringResult[-j] + newStr
##                    newStr = ',' + newStr
##
##                    self._result = newStr
                
            return newStr   
    

##        self._performOperation()
##
##        if len(str(self._result)) < 4:
##            return self._result
##        
##        else: # Atention: Evaluator return an int! This development should take place in the Interpreter(main).
##            
##            stringResult = str(self._result)
##            print(stringResult)
##            stringLength = len(stringResult)
##            newStr = ''
##            for i in range(1, stringLength + 1, 3):
##                #print(i)
##                #print(stringResult[-i])
##                #newStr = stringResult[-i] + ',' + newStr
##                newStr = stringResult[-i] + ',' + newStr
##                while i < len(stringResult):
##                    for j in range(i+1,i+3):
##                        #print(j)
##                        newStr = stringResult[-j] + newStr
##                    newStr = ',' + newStr
##
##            self._result = newStr
##
##        return self._result

        
