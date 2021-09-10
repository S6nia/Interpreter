# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 22 08 21


##
# This module defines the MyParser class.
#

from myNode import MyNode
from myEvaluator import MyEvaluator
from myTokenizer import MyTokenizer

class MyParser:
    '''A parser.'''

    # Docstring?
    def __init__(self, tokens):
        '''(MyParser, list of tokens) -> NoneType'''

        self._tokens = tokens # list of obj of type token
        self._result = 0
        self._nodes = []
        self._tokensConsummed = [] # I'll leave it for later, if I decide to show the tokens consumed in the str repr.

    
    def __str__(self):
        '''(MyParser) -> str

        Return a string representation of the parser.

        >>> tkz = MyTokenizer('+ 1 2')
        >>> tokens = tkz.getListOfTokens()
        >>> psr = MyParser(tokens)
        >>> result = psr.getResult()
        >>> print(psr)
        [] -> Parser -> [['+', 1, 2]]
        '''

        lst = []
 
        for node in self._nodes:
            lst.append([node.getOperator(), node.getLeftOperand(), node.getRightOperand()])

        return str(self._tokens) + ' -> Parser -> ' + str(lst)


    # Docstring?
    # Applying the mutual recursion technique,
    # following the syntax diagrams for evaluating an expression.
    def _getExpression(self):
        '''(MyParser) -> int'''
        
        done = False
        while not done and len(self._tokens) > 0:

            currenToken = self._tokens[0] # token to be analised, current
            currenTokenValue = currenToken.getValue()
            
            if  currenTokenValue == '+' or currenTokenValue == '-':
                self._tokens.pop(0)

                if len(self._tokens) == 1:
                    
                    if currenTokenValue == '+':
                        #refactor
                        node = MyNode(currenTokenValue, self._tokens[0].getValue())
                        self._nodes.append(node1)
                        eva = MyEvaluator(node)
                        return eva.getResult()
                    
                    else:
                        node = MyNode(currenTokenValue, self._tokens[0].getValue())
                        self._nodes.append(node)
                        eva = MyEvaluator(node)
                        return eva.getResult()
                    
                else:
                    value1 = int(self._getFactor())
                    value2 = int(self._getFactor())
                
                if currenTokenValue == '+':
                    node = MyNode(currenTokenValue, value1, value2)
                    self._nodes.append(node)
                    eva = MyEvaluator(node)
                    result =  eva.getResult()
                    
                else:
                    node = MyNode(currenTokenValue, value1, value2)
                    self._nodes.append(node)
                    eva = MyEvaluator(node)
                    result =  eva.getResult()

            elif currenTokenValue == '*' or currenTokenValue == '/':
                result = self._getTerm()

            else:
                done = True
        
        return result

        
    # Docstring?
    def _getTerm(self):
        '''(MyParser) -> int'''

        done = False
        while not done and len(self._tokens) > 0:

            currenToken = self._tokens[0] # token to be analised, current
            currenTokenValue = currenToken.getValue()
            
            if  currenTokenValue == '*' or currenTokenValue == '/':
                self._tokens.pop(0)

                if len(self._tokens) == 1:

                    if currenTokenValue == '*':
                        node = MyNode(currenTokenValue, self._tokens[0].getValue())
                        self._nodes.append(node)
                        eva = MyEvaluator(node)
                        return eva.getResult()
                    
                    else:
                        node = MyNode(currenTokenValue, self._tokens[0].getValue())
                        self._nodes.append(node)
                        eva = MyEvaluator(node)
                        return eva.getResult()
                 
                else:
                    value1 = int(self._getFactor())
                    value2 = int(self._getFactor())

                if currenTokenValue == '*':
                    node = MyNode(currenTokenValue, value1, value2)
                    self._nodes.append(node)
                    eva = MyEvaluator(node)
                    result =  eva.getResult()
                    
                else:
                    node = MyNode(currenTokenValue, value1, value2)
                    self._nodes.append(node)
                    eva = MyEvaluator(node)
                    result =  eva.getResult()

            elif currenTokenValue == '(' or currenTokenValue.isdigit(): 
                result = self._getFactor()

            else:
                done = True

        return result
        

    def _getFactor(self):
        '''(MyParser) -> int'''

        token = self._tokens.pop(0)
        tokenValue = token.getValue()

        if tokenValue == '(':
            result = self._getExpression()
            self._tokens.pop(0)
            
        else:
            result = tokenValue

        return result
 

    def getResult(self):
        '''(MyParser) -> int

        Return the result of the expression.

        >>> tkz = MyTokenizer('+ 1 2')
        >>> tokens = tkz.getListOfTokens()
        >>> psr = MyParser(tokens)
        >>> result = psr.getResult()
        >>> print(result)
        3
        '''

        self._result = self._getExpression() # I could return this directly.
        
        return self._result


# The following segment is executed if this file is to be run.
if __name__ == '__main__':

    # Testing automatically using doctest module.
    import doctest
    doctest.testmod()

    # Creating some examples:
    from myTokenizer import MyTokenizer
    
    # Performing some tests
    #tkz = MyTokenizer('+ 1 2')
    #tkz = MyTokenizer('- 1 2')
    #tkz = MyTokenizer('- 2 1')
    #tkz = MyTokenizer('* 2 3')
    #tkz = MyTokenizer('/ 6 3')
    #tkz = MyTokenizer('+ 11 22')
    #tkz = MyTokenizer('* 2 30') 
    #tkz = MyTokenizer('/ 30 3')
    #tkz = MyTokenizer('-2  1')

    # Testing with parentheses
    #tkz = MyTokenizer('+ (+ 2 3)(+ 2 4)')
    #tkz = MyTokenizer('+ (* 2 3)(* 2 4)')
    #tkz = MyTokenizer('+ 2 3')
    #tkz = MyTokenizer('* 2 3')
    #tkz = MyTokenizer('+ (+ 2 3)(+ (* 2 1) (* 2 2))')
    #tkz = MyTokenizer('- (+ 2 3)(+ (* 2 1) (* 2 2))')
    #tkz = MyTokenizer('- (+ 2 3)(+ (* 2 1) (/ 2 2))')

    # Testing with only one number
    #tkz = MyTokenizer('-12')
    #tkz = MyTokenizer('-1')
    #tkz = MyTokenizer('+123')
    #tkz = MyTokenizer('*2')
    #tkz = MyTokenizer('/2')
    #tkz = MyTokenizer('/ 5 2')

    # While writing the report: 05 09 21
    #tkz = MyTokenizer('+ (+ 2 3)(+ 2 4)(+ 2 3)') # It does not work with more than two operands.
    #tkz = MyTokenizer('*11')
    #tkz = MyTokenizer('/11')
    #tkz = MyTokenizer('+11')
    #tkz = MyTokenizer('-11')

    # More tests on Evaluator: 07 09 21
    #tkz = MyTokenizer('/11')
    #tkz = MyTokenizer('+ 1 2')
    #tkz = MyTokenizer('/123456789')
    #tkz = MyTokenizer('+ 1111111')

    # With commas
    #tkz = MyTokenizer('+11')
    #tkz = MyTokenizer('+111')
    #tkz = MyTokenizer('+1111')
    #tkz = MyTokenizer('+11111')
    #tkz = MyTokenizer('+111111')
    #tkz = MyTokenizer('+1111111')
    #tkz = MyTokenizer('+1111111111')

    # Str repr
    #tkz = MyTokenizer('+11')
    tkz = MyTokenizer('+ 1 2')
    #tkz = MyTokenizer('+ 11 22')
    #tkz = MyTokenizer('* 2 2')
    #tkz = MyTokenizer('+ (* 2 2) (* 2 3)')
    
    
    tokens = tkz.getListOfTokens()
    psr = MyParser(tokens)
    result = psr.getResult()

    print('Result: ' + str(result) + '\n')

    print(psr)

    
    
  
