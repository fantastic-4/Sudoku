import unittest
from Parser.validator import Validator
class Test_validator(unittest.TestCase):
    
    def setUp(self):
        self.validator=Validator()
        
    def test_if_grid_is_well(self):
        self.grid='0030206009003050010018064000081029007000000080067082000026\
09500800203009005010300'
        self.assertTrue(self.validator.validate_values(self.grid))

    def test_if_grid_is_exactly_81(self):
        self.grid='0030206009003050010018064000081029007000000080067082000026\
09500800203009005010300'
        self.assertTrue(self.validator.validate_values(self.grid))

    def test_if_grid_is_wrong(self):
        self.gridwrong='xx020600900305001001806400008102900700000xx8006708200\
002609500800203009005010300'
        print 
        self.assertFalse(self.validator.validate_values(self.gridwrong))

    def test_if_grid_is_empty(self):
        self.gridwrong=''
        self.assertFalse(self.validator.validate_values(self.gridwrong))
        
    def test_if_grid_is_more_than_81(self):
        self.gridwrong='000206009003050010018064000081029007000000080067082000\
02609500800203009005010300111'
        self.assertFalse(self.validator.validate_values(self.gridwrong))
        
    def test_if_grid_is_not_completed(self):
        self.not_completed_grid='003020600305001001806400008102900700000008006\
708200002609500800203009005010300'
        self.assertFalse(self.validator.\
                         validate_values(self.not_completed_grid))
    def test_set_matrix_to_verify(self):
        digits = "123456789"
        rows= "ABCDEFGHI"
        expected_value=['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', \
'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'C1', 'C2', 'C3', 'C4', \
'C5', 'C6', 'C7', 'C8', 'C9', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', \
'D9', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'F1', 'F2', 'F3', \
'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', \
'G8', 'G9', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'I1', 'I2', \
'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
        value=self.validator.set_matrix(rows, digits)
        self.assertEqual(expected_value,value)
        
if __name__ == "__main__":
    unittest.main()
