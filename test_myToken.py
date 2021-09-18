# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 18 09 21


##
# This program tests the MyToken class.
#

import unittest
from myToken import MyToken

class TestMyToken(unittest.TestCase):
    '''Test class for MyToken class.'''

    def test_setValue(self):

        actualToken = MyToken('INT', '1', 1)
        expectedToken = MyToken('INT', '11', 1)

        actualToken.setValue('11')
        self.assertEqual(actualToken.getValue(), expectedToken.getValue())


    def test_getType(self):

        token = MyToken('INT', '11', 1)

        actual = token.getType()
        expected = 'INT'

        self.assertEqual(actual, expected)


    def test_getValue(self):
        
        token = MyToken('INT', '11', 1)

        actual = token.getValue()
        expected = '11'

        self.assertEqual(actual, expected)
        

    def test_getIndex(self):
        
        token = MyToken('INT', '11', 1)

        actual = token.getIndex()
        expected = 1

        self.assertEqual(actual, expected)


    def test_str(self):
         
        token = MyToken('INT', '11', 1)

        actual = str(token)
        expected = 'Token {Type: INT, Value: 11, Index: 1}'

        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main(exit=False)

        
