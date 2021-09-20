# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 19 09 21


##
# This program tests the MyEvaluator class.
#

import unittest
from myEvaluator import MyEvaluator
from myNode import MyNode

class TestMyEvaluator(unittest.TestCase):
    '''Test class for MyEvaluator class.'''


    def test_getResult_oneSingleDigitOperand(self):

        node = MyNode('+', 1)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 2
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_twoSingleDigitOperands(self):

        node = MyNode('+', 1, 2)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 3
        
        self.assertEqual(actualResult, expectedResult)
    

    def test_getResult_oneMultiDigitOperand(self):

        node = MyNode('+', 11)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 22
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_twoMultiDigitOperands(self):

        node = MyNode('+', 11, 22)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 33
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_oneSingleDigitOperand_Multi(self):

        node = MyNode('*', 1)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 1
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_twoSingleDigitOperands_Multi(self):

        node = MyNode('*', 1, 2)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 2
        
        self.assertEqual(actualResult, expectedResult)
    

    def test_getResult_oneMultiDigitOperand_Multi(self):

        node = MyNode('*', 11)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 121
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_twoMultiDigitOperands_Multi(self):

        node = MyNode('*', 11, 22)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 242
        
        self.assertEqual(actualResult, expectedResult)


    def test__performOperation(self):

        node = MyNode('+', 1, 2)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = eva._result
        
        self.assertEqual(actualResult, expectedResult)



    def test__performOperation_valueInstanceVariable(self):

        node = MyNode('+', 1, 2)
        eva = MyEvaluator(node)
        
        actualResult = eva._result
        eva.getResult()
        expectedResult = eva._result

        self.assertNotEqual(actualResult, expectedResult)


    # Tests with nested operations


    def test_str(self):
         
        node = MyNode('+', 1, 2)
        eva = MyEvaluator(node)
        eva.getResult()
         
        actual = str(eva)
        expected = '(+ 1 2) = 3'

        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main(exit=False)

        
