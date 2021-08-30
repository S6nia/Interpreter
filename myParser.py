# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 22 08 21


# Parser verifica de certo modo a ordem dos tokens, eu penso! :) E pensas bem!


##
# This module defines the MyParser class.
#

#from myToken import MyToken

class MyParser:
    '''A parser.'''

    def __init__(self, tokens):

        self._tokens = tokens # list of obj of type token
        self._result = 0


    #def __str__():


    # Following syntax diagrams/grammar <-- Double check this!
    # Applying the mutual recursion technique:
    def _getExpression(self):

        done = False
        while not done and len(self._tokens) > 0:

            currenToken = self._tokens[0] # token to be analised, current
            currenTokenValue = currenToken.getValue()
            
            if  currenTokenValue == '+' or currenTokenValue == '-':
                self._tokens.pop(0)
                value1 = int(self._getFactor())
                value2 = int(self._getFactor())

                if currenTokenValue == '+':
                    result = value1 + value2
                    
                else:
                    result = value1 - value2

            elif currenTokenValue != '+' or currenTokenValue != '-':
                result = self._getTerm()

            else:
                done = True
        
        return result
        

    def _getTerm(self):

        done = False
        while not done and len(self._tokens) > 0:

            currenToken = self._tokens[0] # token to be analised, current
            currenTokenValue = currenToken.getValue()
            
            if  currenTokenValue == '*' or currenTokenValue == '/':
                self._tokens.pop(0)
                value1 = int(self._getFactor())
                value2 = int(self._getFactor())

                if currenTokenValue == '*':
                    result = value1 * value2
                else:
                    result = value1 / value2

            elif currenTokenValue != '*' or currenTokenValue != '/': 
                result = self._getFactor()

            else:
                done = True

        return result
        

    def _getFactor(self):

        token = self._tokens.pop(0) # error message subscriptable! lol
        tokenValue = token.getValue()

        if tokenValue.isdigit():
            return tokenValue


    def getResult(self):

        self._result = self._getExpression() # I could return this directly.
                                             # Let's see if I'll need this property in the future...

        return self._result


if __name__ == '__main__':

    from myTokenizer import MyTokenizer

    # Performing some tests:
    tkz = MyTokenizer('+ 1 2') #F #P
    #tkz = MyTokenizer('- 1 2') #F #P #Accepts negatives
    #tkz = MyTokenizer('- 2 1') #- #P
    #tkz = MyTokenizer('* 2 3') #P #P
    #tkz = MyTokenizer('/ 6 3') #P #P
    #tkz = MyTokenizer('+ 11 22')#F #P
    #tkz = MyTokenizer('* 2 30') #P #P
    #tkz = MyTokenizer('/ 30 3') #P #P
    #tkz = MyTokenizer('-2  1')   #- #P
    
    tokens = tkz.getListOfTokens()
    psr = MyParser(tokens)
    result = psr.getResult()
    print('Result: ', result)
    
