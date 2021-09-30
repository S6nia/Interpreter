# Name: Sonia Gonçalves
# Program: MSc IT
# ST ID: 13106604
# Date: September 2021


##
# This program tests the MyEvaluator class.
#

import unittest
from myEvaluator import MyEvaluator
from myNode import MyNode


class TestMyEvaluator(unittest.TestCase):
    '''Test class for MyEvaluator class.'''

    def test_getResult_oneSingleDigitOperand_Addition(self):

        node = MyNode('+', 1)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 2
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_twoSingleDigitOperands_Addition(self):

        node = MyNode('+', 1, 2)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 3
        
        self.assertEqual(actualResult, expectedResult)
    

    def test_getResult_oneMultiDigitOperand_Addition(self):

        node = MyNode('+', 11)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 22
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_twoMultiDigitOperands_Addition(self):

        node = MyNode('+', 11, 22)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 33
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_oneSingleDigitOperand_Subtr(self):

        node = MyNode('-', 1)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 0
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_twoSingleDigitOperands_Subtr(self):

        node = MyNode('-', 2, 1)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 1
        
        self.assertEqual(actualResult, expectedResult)
    

    def test_getResult_oneMultiDigitOperand_Subtr(self):

        node = MyNode('-', 11)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 0
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_twoMultiDigitOperands_Subtr(self):

        node = MyNode('-', 22, 11)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 11
        
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


    def test_getResult_oneSingleDigitOperand_Div(self):

        node = MyNode('/', 1)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 1
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_twoSingleDigitOperands_Div(self):

        node = MyNode('/', 2, 1)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 2
        
        self.assertEqual(actualResult, expectedResult)
    

    def test_getResult_oneMultiDigitOperand_Div(self):

        node = MyNode('/', 11)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 1
        
        self.assertEqual(actualResult, expectedResult)


    def test_getResult_twoMultiDigitOperands_Div(self):

        node = MyNode('/', 22, 11)
        eva = MyEvaluator(node)
        actualResult = eva.getResult()

        expectedResult = 2
        
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


    def test_str(self):
         
        node = MyNode('+', 1, 2)
        eva = MyEvaluator(node)
        eva.getResult()
         
        actual = str(eva)
        expected = '(+ 1 2) = 3'

        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main(exit=False)

        
