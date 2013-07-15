import unittest
from Main.grid import Grid

class Test_grid(unittest.TestCase):


    def setUp(self):
        self.gridA="003020600900305001001806400008102900700000008006708200002609500800203009005010300"
        self.gridB="""400000805
                      030000000
                      000700000
                      020000060
                      000080400
                      000010000
                      000603070
                      500200000
                      104000000"""
                      
        self.wrong_grid = "333020600900305001001806400008102900700000008006708200002609500800203009005010300"
        self.GridHard="52...6.........7.13...........4..8..6......5...........418.........3..2...87....."
        self.grid_expected={'I6': '0', 'H9': '9', 'I2': '0', 'E8': '0', 'H3': '0', 'H7': '0', 'I7': '3', 'I4': '0', 'H5': '0', 'F9': '0', 'G7': '5', 'G6': '9', 'G5': '0', 'E1': '7', 'G3': '2', 'G2': '0', 'G1': '0', 'I1': '0', 'C8': '0', 'I3': '5', 'E5': '0', 'I5': '1', 'C9': '0', 'G9': '0', 'G8': '0', 'A1': '0', 'A3': '3', 'A2': '0', 'A5': '2', 'A4': '0', 'A7': '6', 'A6': '0', 'C3': '1', 'C2': '0', 'C1': '0', 'E6': '0', 'C7': '4', 'C6': '6', 'C5': '0', 'C4': '8', 'I9': '0', 'D8': '0', 'I8': '0', 'E4': '0', 'D9': '0', 'H8': '0', 'F6': '8', 'A9': '0', 'G4': '6', 'A8': '0', 'E7': '0', 'E3': '0', 'F1': '0', 'F2': '0', 'F3': '6', 'F4': '7', 'F5': '0', 'E2': '0', 'F7': '2', 'F8': '0', 'D2': '0', 'H1': '8', 'H6': '3', 'H2': '0', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '0', 'B6': '5', 'B7': '0', 'E9': '8', 'B1': '9', 'B2': '0', 'B3': '0', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '0', 'B8': '0', 'B9': '1', 'D1': '0'}
        self.Expected_HardGrid={'I6': '.', 'H9': '.', 'I2': '.', 'E8': '5', 'H3': '.', 'H7': '.', 'I7': '.', 'I4': '7', 'H5': '3', 'F9': '.', 'G7': '.', 'G6': '.', 'G5': '.', 'E1': '6', 'G3': '1', 'G2': '4', 'G1': '.', 'I1': '.', 'C8': '.', 'I3': '8', 'E5': '.', 'I5': '.', 'C9': '.', 'G9': '.', 'G8': '.', 'A1': '5', 'A3': '.', 'A2': '2', 'A5': '.', 'A4': '.', 'A7': '.', 'A6': '6', 'C3': '.', 'C2': '.', 'C1': '3', 'E6': '.', 'C7': '.', 'C6': '.', 'C5': '.', 'C4': '.', 'I9': '.', 'D8': '.', 'I8': '.', 'E4': '.', 'D9': '.', 'H8': '2', 'F6': '.', 'A9': '.', 'G4': '8', 'A8': '.', 'E7': '.', 'E3': '.', 'F1': '.', 'F2': '.', 'F3': '.', 'F4': '.', 'F5': '.', 'E2': '.', 'F7': '.', 'F8': '.', 'D2': '.', 'H1': '.', 'H6': '.', 'H2': '.', 'H4': '.', 'D3': '.', 'B4': '.', 'B5': '.', 'B6': '.', 'B7': '7', 'E9': '.', 'B1': '.', 'B2': '.', 'B3': '.', 'D6': '.', 'D7': '8', 'D4': '4', 'D5': '.', 'B8': '.', 'B9': '1', 'D1': '.'}
        self.grid=Grid()

        
     
    def test_units(self):
        "A set of tests that must pass."
        self.assertEqual(81,len(self.grid.squares))
        self.assertEqual(27,len(self.grid.unitlist))
        assert all(len(self.grid.units[s]) == 3 for s in self.grid.squares)
        assert all(len(self.grid.peers[s]) == 20 for s in self.grid.squares)
        assert self.grid.units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                               ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                               ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
        assert self.grid.peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                                   'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                                   'A1', 'A3', 'B1', 'B3'])
                    
 
    def test_if_set_values_can_handle_empty_grid(self):
        grid=''
        grid1 = self.grid.validate_grid(grid)
        self.assertFalse(grid1)
 
    def test_if_set_values_can_handle_wrong_grid(self):
        grid='ss30206009003050010018064000081029007000000080067082000026095008002030090050103xx'
        grid1 = self.grid.validate_grid(grid)
        self.assertFalse(grid1)
 
         
    def test_if_set_values_inserts_correct_squares_easy_grid(self):
        grid1 = self.grid.set_values(self.gridA)
        self.assertEqual(self.grid_expected,grid1)
 
    def test_the_display_method_in_grid_prints_correct_format(self):
        gridX={'I6': '0', 'H9': '9', 'I2': '0', 'E8': '0', 'H3': '0', 'H7': '0', 'I7': '3', 'I4': '0', 'H5': '0', 'F9': '0', 'G7': '5', 'G6': '9', 'G5': '0', 'E1': '7', 'G3': '2', 'G2': '0', 'G1': '0', 'I1': '0', 'C8': '0', 'I3': '5', 'E5': '0', 'I5': '1', 'C9': '0', 'G9': '0', 'G8': '0', 'A1': '0', 'A3': '3', 'A2': '0', 'A5': '2', 'A4': '0', 'A7': '6', 'A6': '0', 'C3': '1', 'C2': '0', 'C1': '0', 'E6': '0', 'C7': '4', 'C6': '6', 'C5': '0', 'C4': '8', 'I9': '0', 'D8': '0', 'I8': '0', 'E4': '0', 'D9': '0', 'H8': '0', 'F6': '8', 'A9': '0', 'G4': '6', 'A8': '0', 'E7': '0', 'E3': '0', 'F1': '0', 'F2': '0', 'F3': '6', 'F4': '7', 'F5': '0', 'E2': '0', 'F7': '2', 'F8': '0', 'D2': '0', 'H1': '8', 'H6': '3', 'H2': '0', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '0', 'B6': '5', 'B7': '0', 'E9': '8', 'B1': '9', 'B2': '0', 'B3': '0', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '0', 'B8': '0', 'B9': '1', 'D1': '0'}
        print self.grid.display(gridX)  
 
    def test_if_set_values_inserts_correct_squares_hard_grid(self):
        grid1 = self.grid.set_values(self.GridHard)
        self.assertEqual(self.Expected_HardGrid,grid1)

    def test_if_correct_grid_returns_true(self):
        self.assertTrue(self.grid.validate_grid(self.gridA))
        
    def test_if_wrong_grid_returns_false(self):
        self.assertFalse(self.grid.validate_grid(self.wrong_grid))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
