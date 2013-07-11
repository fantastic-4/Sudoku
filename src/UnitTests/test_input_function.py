import unittest
from Main.input_grid import validate_text

class Test_input_function(unittest.TestCase):

    def setUp(self):        
        self.one_character = "1"
        self.fifty_characters = "74236815939657124858149236781475392697528643126314"
        self.expected_text_with_one_character = "100000000000000000000000000000000000000000000000000000000000000000000000000000000"
        self.expected_text_with_fifty_characters = "742368159396571248581492367814753926975286431263140000000000000000000000000000000"
        
    def test_if_one_character_is_completed_with_zeroes(self):
        self.assertTrue(validate_text(self.one_character) == self.expected_text_with_one_character)

    def test_if_fifty_characters_are_completed_with_zeroes(self):
        self.assertTrue(validate_text(self.fifty_characters) == self.expected_text_with_fifty_characters)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()