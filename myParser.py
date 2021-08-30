# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 22 08 21


# Parser verifica de certo modo a ordem dos tokens, eu penso! :)


##
# This module defines the MyParser class.
#

#from myToken import MyToken

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
        #result = self._getTerm()

##        done = False
##        while not done and len(self._tokens) > 0:
##
##            currenToken = self._tokens[0] # token to be analised, current
##            currenTokenValue = currenToken.getValue()
##            print(currenTokenValue)
##            
##            if  currenTokenValue == '+':
##
##                test = self._tokens.pop(0)
##                print(test)
##                value1 = int(self._getTerm())
##                print(value1)
##                value2 = int(self._getTerm())
##                print(value2)
##                result = value1 + value2
##                print(result)
##
##            elif currenTokenValue == '-':
##                
##                test = self._tokens.pop(0)
##                print(test)
##                value1 = self._getTerm()
##                value2 = self._getTerm()
##                result = value1 - value2
##
##            else:
##                #result = self._getTerm()
##                done = True
##
##        #result = self._getTerm()
##        
##        return result


        done = False
        while not done and len(self._tokens) > 0:

            currenToken = self._tokens[0] # token to be analised, current
            currenTokenValue = currenToken.getValue()
            print(currenTokenValue)
            
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
                #result = self._getTerm()
                done = True

        #result = self._getTerm()
        
        return result
        

    def _getTerm(self):

        done = False
        while not done and len(self._tokens) > 0:

            currenToken = self._tokens[0] # token to be analised, current
            currenTokenValue = currenToken.getValue()
            print(currenTokenValue)
            
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

        
##
##        result = self._getFactor()
##
##        if not result.isdigit():
##            done = False
##            while not done and len(self._tokens) > 0:
##
##                currenToken = self._tokens[0] # token to be analised, current
##                currenTokenValue = currenToken.getValue()
##                if  currenTokenValue == '*' or  currenTokenValue == '/':
##                    self._tokens.pop(0)
##                    value1 = int(self._getFactor())
##                    value2 = int(self._getFactor())
##
##                    if currenTokenValue == '*':
##                        result = value1 * value2
##
##                    else:
##                        result = value1 / value2
##
##                else:
##                    done = True
##
##            return result
##        else:
##            return result
        

    def _getFactor(self):

        token = self._tokens.pop(0) # error message subscriptable! lol
        print(token)
        tokenValue = token.getValue()
        print(tokenValue)

        if tokenValue.isdigit():
            return tokenValue
        #else:
        #    return tokenValue


    def getResult(self):

        self._result = self._getExpression()
        print(self._result)

        return self._result


if __name__ == '__main__':

    from myTokenizer import MyTokenizer

    #tkz = MyTokenizer('+ 1 2') #F 
    #tkz = MyTokenizer('- 1 2') #F
    #tkz = MyTokenizer('* 2 3') #P
    #tkz = MyTokenizer('/ 6 3') #P
    #tkz = MyTokenizer('+ 11 22')
    tkz = MyTokenizer('* 2 30') #P
    #tkz = MyTokenizer('/ 30 3') #P
    
    tokens = tkz.getListOfTokens()
    psr = MyParser(tokens)
    result = psr.getResult()
    print('Result: ', result)
    
