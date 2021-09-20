# Name: Sonia Gonçalves
# Program: IT MSc
# ST ID: 
# Date: 19 09 21


##
# This program tests the MyTokenizer class.
#

import unittest
from myTokenizer import MyTokenizer

class TestMyTokenizer(unittest.TestCase):
    '''Test class for MyTokenizer class.'''
    

    def test_getListOfTokens(self):

        tkz = MyTokenizer('+ 1 2')
        lisTokens = tkz.getListOfTokens()

        actualValueTokens = []
        for i in range(len(lisTokens)):
            actualValueTokens.append(lisTokens[i].getValue())
             
        expectedValueTokens = ['+', '1', '2']
        
        self.assertEqual(actualValueTokens, expectedValueTokens)


    def test__creaTokens(self):

        tkz = MyTokenizer('+ 1 2')
        actuaLisTokens = tkz.getListOfTokens()

        expectedLisTokens = tkz._output # private instance variable (should use accessor)

        self.assertEqual(actuaLisTokens, expectedLisTokens)


    def test__creaTokens_valueInstanceVariable(self):

        tkz = MyTokenizer('+ 1 2')
        
        actuaLisTokens = tkz._output
        tkz.getListOfTokens()
        expectedLisTokens = tkz._output

        self.assertEqual(actuaLisTokens, expectedLisTokens)


    def test_str(self):
         
        tkz = MyTokenizer('+ 1 2')
        tkz.getListOfTokens()
         
        actual = str(tkz)
        expected = "'+ 1 2' -> Tokenizer -> ['+', '1', '2']"

        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main(exit=False)

        
