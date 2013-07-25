import unittest

from Main.grid_generator import GridGenerator
from mockito import when, unstub

class Test_grid_generator(unittest.TestCase):
    
    def setUp(self):
        self.generator = GridGenerator()
        
        when(self.generator).get_random_integer().thenReturn(0).thenReturn(1).thenReturn(2).thenReturn(3).thenReturn(4).thenReturn(5).thenReturn(6).thenReturn(7).thenReturn(8)
        when(self.generator).get_random_row().thenReturn("A")
        when(self.generator).get_random_column().thenReturn("1").thenReturn("2").thenReturn("3")
        
        self.expected_grid = {'B8': '2', 'H1': '6', 'C7': '4', 'B3': '6',
                              'D3': '4', 'G9': '8', 'G8': '7', 'B9': '3',
                              'A3': '3', 'G7': '9', 'G6': '2', 'G5': '4',
                              'G4': '6', 'G3': '1', 'G2': '3', 'G1': '5',
                              'B5': '8', 'I1': '9', 'I3': '8', 'I2': '7',
                              'I5': '3', 'I4': '5', 'I7': '6', 'I6': '1',
                              'A1': '1', 'C9': '6', 'C8': '5', 'A5': '5',
                              'E8': '1', 'A7': '7', 'A6': '6', 'E5': '9',
                              'C2': '8', 'C1': '7', 'E6': '7', 'E1': '3',
                              'A2': '2', 'C5': '2', 'A4': '4', 'I9': '2',
                              'B2': '5', 'I8': '4', 'H2': '4', 'D9': '7',
                              'F2': '9', 'D5': '6', 'C3': '9', 'A9': '9',
                              'C6': '3', 'E4': '8', 'B1': '4', 'E7': '2',
                              'F1': '8', 'H8': '3', 'H9': '1', 'F4': '2',
                              'F5': '1', 'F6': '4', 'F7': '3', 'F8': '6',
                              'H3': '2', 'F3': '7', 'H6': '8', 'H7': '5',
                              'H4': '9', 'H5': '7', 'B4': '7', 'A8': '8',
                              'B6': '9', 'B7': '1', 'E9': '4', 'E3': '5',
                              'D8': '9', 'F9': '5', 'D6': '5', 'D7': '8',
                              'D4': '3', 'C4': '1', 'D2': '1', 'E2': '6',
                              'D1': '2'}
        self.square = "A"
        self.expected_square_1 = "1"
        self.expected_square_2 = "2"
        self.expected_square_3 = "3"
        
        self.difficult_easy = "Easy"
        self.difficult_medium = "Medium"
        self.difficult_hard = "Hard"
        
    def test_if_a_grid_can_be_generated(self):

        self.assertDictEqual(self.generator.generate_grid(), self.expected_grid)
        
    def test_if_hints_number_is_according_to_difficulty_given_as_easy(self):
        
        when(self.generator).get_hints_quantity(self.difficult_easy).thenReturn(1)
        self.generator.generate_grid()
        expected_value =  self.generator.values_chooser(self.difficult_easy)[self.square\
                                                                + self.expected_square_1]
        self.assertTrue(expected_value,self.expected_square_1)
    
    def test_if_hints_number_is_according_to_difficulty_given_as_medium(self):
        
        
        when(self.generator).get_hints_quantity(self.difficult_medium).thenReturn(2)
        self.generator.generate_grid()
        expected_value =  self.generator.values_chooser(self.difficult_medium)[self.square\
                                                                + self.expected_square_2]
        self.assertTrue(expected_value,self.expected_square_2)
        
    def test_if_hints_number_is_according_to_difficulty_given_as_hard(self):
        
        when(self.generator).get_hints_quantity(self.difficult_hard).thenReturn(3)
        self.generator.generate_grid()
        expected_value =  self.generator.values_chooser("Hard")[self.square\
                                                                + self.expected_square_3]
        self.assertTrue(expected_value,self.expected_square_3)
       
    def tearDown(self):
        unstub()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()