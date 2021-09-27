# Name: Sonia Gonçalves
# Program: MSc IT
# ST ID: 13106604
# Date: September 2021


##
# This module defines the MyParser class.
#

from myNode import MyNode
from myEvaluator import MyEvaluator
from myTokenizer import MyTokenizer


class MyParser:
    '''A parser.'''

    def __init__(self, tokens):
        '''(MyParser, list of tokens) -> NoneType'''

        self._tokens = tokens # list of obj of type token
        self._result = 0
        self._nodes = []


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
            if node.getRightOperand() != None:
                lst.append([node.getOperator(), node.getLeftOperand(), node.getRightOperand()])
            else:
                lst.append([node.getOperator(), node.getLeftOperand()])

        return str(self._tokens) + ' -> Parser -> ' + str(lst)


    # Applying the mutual recursion technique,
    # following the syntax diagrams for evaluating an expression: Expression -> Term -> Factor.
    def _getExpression(self):
        '''(MyParser) -> int'''
        
        done = False
        while not done and len(self._tokens) > 0:

            currenToken = self._tokens[0] # token to be analised, current
            currenTokenValue = currenToken.getValue()
            
            if  currenTokenValue == '+' or currenTokenValue == '-':
                self._tokens.pop(0)

                # After removing the operator,
                # if the len of list of tokens is zero, raise an error.
                if len(self._tokens) == 0:
                    raise SyntaxError("Unexpected end.")

                # If the len of list of tokens is one,
                # then create a node and an evaluator to evaluate one expression with only one number.
                elif len(self._tokens) == 1:

                    # If the second token is not a digit, raise an error.
                    if not self._tokens[0].getValue().isdigit():
                        raise SyntaxError("Invalid expression.")
                    
                    if currenTokenValue == '+':
                        #refactor
                        node = MyNode(currenTokenValue, self._tokens[0].getValue())
                        self._tokens.pop(0)
                        self._nodes.append(node)
                        eva = MyEvaluator(node)
                        return eva.getResult()
                    
                    else:
                        node = MyNode(currenTokenValue, self._tokens[0].getValue())
                        self._tokens.pop(0)
                        self._nodes.append(node)
                        eva = MyEvaluator(node)
                        return eva.getResult()
                    
                else:

                    # If the len of the list of tokens is greater than one,
                    # determine the values of the operands.
                    if self._tokens[0].getValue().isdigit() or self._tokens[0].getValue() == '(':
                        value1 = int(self._getFactor())
                        value2 = int(self._getFactor())
                        
                    else:
                        # For other exceptions, raise an error.
                        raise SyntaxError("Invalid expression.")
                
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

        
    def _getTerm(self):
        '''(MyParser) -> int'''

        done = False
        while not done and len(self._tokens) > 0:

            currenToken = self._tokens[0] # token to be analised, current
            currenTokenValue = currenToken.getValue()
            
            if  currenTokenValue == '*' or currenTokenValue == '/':
                self._tokens.pop(0)

                # After removing the operator,
                # if the len of list of tokens is zero, raise an error.
                if len(self._tokens) == 0:
                    raise SyntaxError("Unexpected end.")

                # If the len of list of tokens is one,
                # then create a node and an evaluator to evaluate one expression with only one number.
                elif len(self._tokens) == 1:

                    # If the second token is not a digit, raise an error.
                    if not self._tokens[0].getValue().isdigit():
                        raise SyntaxError("Invalid expression.")

                    if currenTokenValue == '*':
                        node = MyNode(currenTokenValue, self._tokens[0].getValue())
                        self._tokens.pop(0)
                        self._nodes.append(node)
                        eva = MyEvaluator(node)
                        return eva.getResult()
                    
                    else:
                        node = MyNode(currenTokenValue, self._tokens[0].getValue())
                        self._tokens.pop(0)
                        self._nodes.append(node)
                        eva = MyEvaluator(node)
                        return eva.getResult()
                 
                else:

                    # If the len of the list of tokens is greater than one,
                    # determine the values of the operands.
                    if self._tokens[0].getValue().isdigit() or self._tokens[0].getValue() == '(':
                        value1 = int(self._getFactor())
                        value2 = int(self._getFactor())
                        
                    else:
                        # For other exceptions, raise an error.
                        raise SyntaxError("Invalid expression.")

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

        self._result = self._getExpression()
        
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
    #tkz = MyTokenizer('+ 1 2')
    #tkz = MyTokenizer('+ 11 22')
    #tkz = MyTokenizer('* 2 2')
    tkz = MyTokenizer('+ (* 2 2) (* 2 3)')
    
    tokens = tkz.getListOfTokens()
    psr = MyParser(tokens)
    result = psr.getResult()

    print('Result: ' + str(result) + '\n')

    print(psr)

    
