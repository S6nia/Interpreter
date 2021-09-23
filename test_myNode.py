# Name: Sonia Gonçalves
# Program: MSc IT
# ST ID: 13106604
# Date: September 2021


##
# This program tests the MyNode class.
#

import unittest
from myNode import MyNode


class TestMyNode(unittest.TestCase):
    '''Test class for MyNode class.'''

    def test_getOperator_singleOperand(self):

        node = MyNode('+', 1)

        actual = node.getOperator()
        expected = '+'

        self.assertEqual(actual, expected)


    def test_getLeft_singleOperand(self):
        
        node = MyNode('+', 1)

        actual = node.getLeftOperand()
        expected = 1

        self.assertEqual(actual, expected)
        

    def test_getRightOperand_singleOperand(self):
        
        node = MyNode('+', 1)

        actual = node.getRightOperand()
        expected = None

        self.assertEqual(actual, expected)


    def test_str_singleOperand(self):
         
        node = MyNode('+', 1)

        actual = str(node)
        expected = 'Node {Operator: +, Value: 1}'

        self.assertEqual(actual, expected)
    

    def test_getOperator_withTwOperands(self):

        node = MyNode('+', 1, 2)

        actual = node.getOperator()
        expected = '+'

        self.assertEqual(actual, expected)


    def test_getLeftOperand_withTwOperands(self):
        
        node = MyNode('+', 1, 2)

        actual = node.getLeftOperand()
        expected = 1

        self.assertEqual(actual, expected)
        

    def test_getRightOperand_withTwOperands(self):
        
        node = MyNode('+', 1, 2)

        actual = node.getRightOperand()
        expected = 2

        self.assertEqual(actual, expected)


    def test_str_withTwOperands(self):
         
        node = MyNode('+', 1, 2)

        actual = str(node)
        expected = 'Node {Operator: +, Left value: 1, Right value: 2}'

        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main(exit=False)

        
