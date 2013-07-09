import unittest
from Main.validate import Validate
class Test_validate_class(unittest.TestCase):
    
    def setUp(self):
        self.validate=Validate()
        
    def test_if_grid_is_well(self):
        self.grid='003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.assertTrue(self.validate.validate_values(self.grid))

    def test_if_grid_is_exactly_81(self):
        self.grid='003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.assertTrue(self.validate.validate_values(self.grid))

    def test_if_grid_is_wrong(self):
        self.gridwrong='xx020600900305001001806400008102900700000xx8006708200002609500800203009005010300'
        print 
        self.assertFalse(self.validate.validate_values(self.gridwrong))

    def test_if_grid_is_empty(self):
        self.gridwrong=''
        self.assertFalse(self.validate.validate_values(self.gridwrong))
        
    def test_if_grid_is_more_than_81(self):
        self.gridwrong='00020600900305001001806400008102900700000008006708200002609500800203009005010300111'
        self.assertFalse(self.validate.validate_values(self.gridwrong))
        
    def test_if_grid_is_not_completed(self):
        self.not_completed_grid='003020600305001001806400008102900700000008006708200002609500800203009005010300'
        self.assertFalse(self.validate.validate_values(self.not_completed_grid))
        
if __name__ == "__main__":
    unittest.main()
