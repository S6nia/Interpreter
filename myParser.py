# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 22 08 21


# Parser verifica de certo modo a ordem dos tokens, eu penso! :)


##
# This module defines the MyParser class.
#

from myToken import MyToken

class MyParser:
    '''A parser.'''

    def __init__(self, tokens):

        self._tokens = tokens # list of obj of type token
        #self._firstToken = self._tokens[0].getValue()
        #self._node = node
        self._result = 0


    #def __str__():
    

    # Following syntax diagrams/grammar <-- check this
    def _getExpression(self):

        #value = self._getTerm()
        #result = 0

        done = False
        while not done and len(self._tokens) > 0:

            currenToken = self._tokens[0] # token to be analised, current
            currenTokenValue = currenToken.getValue()
            print(currenTokenValue)
            
            if  currenTokenValue == '+':

                test = self._tokens.pop(0)
                print(test)
                value1 = int(self._getTerm())
                print(value1)
                value2 = int(self._getTerm())
                print(value2)
                result = value1 + value2
                print(result)

            elif currenTokenValue == '-':
                
                test = self._tokens.pop(0)
                print(test)
                value1 = self._getTerm()
                value2 = self._getTerm()
                result = value1 - value2

            else:
                done = True

        return result
        

    def _getTerm(self):

        result = self._getFactor()

        done = False
        while not done and len(self._tokens) > 0:

            currenToken = self._tokens[0] # token to be analised, current
            currenTokenValue = currenToken.getValue()
            if  currenTokenValue == '*' or  currenTokenValue == '/':
                self._tokens.pop(0)
                value1 = self._getFactor()
                value2 = self._getFactor()

                if currenTokenValue == '*':
                    result = value1 * value2

                else:
                    result = value1 / value2

            else:
                done = True

        return result
        

    def _getFactor(self):

        token = self._tokens.pop(0) # error message subscriptable! lol
        print(token)
        tokenValue = token.getValue()
        print(tokenValue)

        if tokenValue.isdigit():
            return tokenValue


    def getResult(self):

        self._result = self._getExpression()
        print(self._result)

        return self._result


if __name__ == '__main__':

    from myTokenizer import MyTokenizer

    tkz = MyTokenizer('+ 1 2')
    tokens = tkz.getListOfTokens()
    psr = MyParser(tokens)
    result = psr.getResult()
    print('Result: ', result)
    
