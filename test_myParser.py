# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 19 09 21


##
# This program tests the MyParser class.
#

import unittest
from myParser import MyParser
from myTokenizer import MyTokenizer

class TestMyParser(unittest.TestCase):
    '''Test class for MyParser class.'''
    

    def test_getResult1(self):

        tkz = MyTokenizer('+ 1 2')
        tokens = tkz.getListOfTokens()
        psr = MyParser(tokens)

        actualResult = psr.getResult()
        expectedResult = 3
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult2(self):

        tkz = MyTokenizer('+ 1 2')
        tokens = tkz.getListOfTokens()
        psr = MyParser(tokens)

        actualResult = psr._result
        psr.getResult()
        expectedResult = psr._result
        
        self.assertNotEqual(actualResult, expectedResult)


    # Tests _getExpression, _getTerm, _getFactor !?


    def test_str(self):
         
        tkz = MyTokenizer('+ 1 2')
        tokens = tkz.getListOfTokens()
        
        psr = MyParser(tokens)
        psr.getResult()
         
        actual = str(psr)
        expected = "[] -> Parser -> [['+', 1, 2]]"

        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main(exit=False)

        
