# Name: Sonia Gonçalves
# Program: MSc IT
# ST ID: 13106604
# Date: September 2021


##
# This program tests the MyParser class.
#

import unittest
from myParser import MyParser
from myTokenizer import MyTokenizer


class TestMyParser(unittest.TestCase):
    '''Test class for MyParser class.'''
    
    def test_getResult(self):

        tkz = MyTokenizer('+ 1 2')
        tokens = tkz.getListOfTokens()
        psr = MyParser(tokens)

        actualResult = psr.getResult()
        expectedResult = 3
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_valueInstanceVariable(self):

        tkz = MyTokenizer('+ 1 2')
        tokens = tkz.getListOfTokens()
        psr = MyParser(tokens)

        # private instance variable (should use accessor, but it is not implemented)
        actualResult = psr._result
        psr.getResult()
        expectedResult = psr._result
        
        self.assertNotEqual(actualResult, expectedResult)


    def test_str(self):
         
        tkz = MyTokenizer('+ 1 2')
        tokens = tkz.getListOfTokens()
        
        psr = MyParser(tokens)
        psr.getResult()
         
        actual = str(psr)
        expected = "[] -> Parser -> [['+', 1, 2]]"

        self.assertEqual(actual, expected)


    def test_getResult_withParentheses(self):

        tkz = MyTokenizer('+ (* 2 2) (* 2 3)')
        tokens = tkz.getListOfTokens()
        psr = MyParser(tokens)

        actualResult = psr.getResult()
        expectedResult = 10
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_valueInstanceVariable_withParentheses(self):

        tkz = MyTokenizer('+ (* 2 2) (* 2 3)')
        tokens = tkz.getListOfTokens()
        psr = MyParser(tokens)

        actualResult = psr._result
        psr.getResult()
        expectedResult = psr._result
        
        self.assertNotEqual(actualResult, expectedResult)


    def test_str_withParentheses(self):
         
        tkz = MyTokenizer('+ (* 2 2) (* 2 3)')
        tokens = tkz.getListOfTokens()
        
        psr = MyParser(tokens)
        psr.getResult()
         
        actual = str(psr)
        expected = "[] -> Parser -> [['*', 2, 2], ['*', 2, 3], ['+', 4, 6]]"

        self.assertEqual(actual, expected)


    def test_getResult_nestedParentheses(self):

        tkz = MyTokenizer('+ (+ 2 3)(+ (* 2 1) (* 2 2))')
        tokens = tkz.getListOfTokens()
        psr = MyParser(tokens)

        actualResult = psr.getResult()
        expectedResult = 11
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_valueInstanceVariable_nestedParentheses(self):

        tkz = MyTokenizer('+ (+ 2 3)(+ (* 2 1) (* 2 2))')
        tokens = tkz.getListOfTokens()
        psr = MyParser(tokens)

        actualResult = psr._result
        psr.getResult()
        expectedResult = psr._result
        
        self.assertNotEqual(actualResult, expectedResult)


    def test_str_nestedParentheses(self):
         
        tkz = MyTokenizer('+ (+ 2 3)(+ (* 2 1) (* 2 2))')
        tokens = tkz.getListOfTokens()
        
        psr = MyParser(tokens)
        psr.getResult()
         
        actual = str(psr)
        expected = "[] -> Parser -> [['+', 2, 3], ['*', 2, 1], ['*', 2, 2], ['+', 2, 4], ['+', 5, 6]]"

        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main(exit=False)

        
