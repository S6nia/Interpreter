# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 18 09 21


##
# This program tests the MyNode class.
#

import unittest
from myNode import MyNode

class TestMyNode(unittest.TestCase):
    '''Test class for MyNode class.'''
    

    def test_getOperator(self):

        node = MyNode('+', 1, 2)

        actual = node.getOperator()
        expected = '+'

        self.assertEqual(actual, expected)


    def test_getLeftOperand(self):
        
        node = MyNode('+', 1, 2)

        actual = node.getLeftOperand()
        expected = 1

        self.assertEqual(actual, expected)
        

    def test_getRightOperand(self):
        
        node = MyNode('+', 1, 2)

        actual = node.getRightOperand()
        expected = 2

        self.assertEqual(actual, expected)


    def test_str(self):
         
        node = MyNode('+', 1, 2)

        actual = str(node)
        expected = 'Node {Operator: +, Left value: 1, Right value: 2}'

        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main(exit=False)

        
