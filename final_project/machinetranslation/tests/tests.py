import unittest

from translator import english_to_french, french_to_english

class Test_english_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Null'), 'Null') # test that when Null is sent, that Null is received
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when Hello is given in English that the output is Bonjour in French

class Test_french_to_english(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english('Null'), 'Null') # test that when Null is sent, that Null is received
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when Bonjour is given in French that the output is Hello in English

unittest.main()