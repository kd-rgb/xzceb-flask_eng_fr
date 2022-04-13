import unittest

from translator import englishToFrench, frenchToEnglish

class Test_englishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Null'), 'Null') # test that when Null is sent, that Null is received
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # test when Hello is given in English that the output is Bonjour in French

class Test_frenchToEnglish(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(frenchToEnglish('Null'), 'Null') # test that when Null is sent, that Null is received
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when Bonjour is given in French that the output is Hello in English

unittest.main()