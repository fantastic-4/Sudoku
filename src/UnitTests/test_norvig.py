import unittest
from Solver.norvig import Norvig
from Main.grid import Grid


class Test_norvig(unittest.TestCase):


    def setUp(self):
        self.norvig=Norvig()
        self.grid=Grid()


    def test_solve_a_easy_grid_using_norvig(self):
        self.gridA='003020600900305001001806400008102900700000008006708200002609500800203009005010300' 
        grid2=self.norvig.solve(self.gridA)
        gridA_expected=grid2
        self.assertEquals(gridA_expected,grid2)
         
         
 
    def test_solve_a_Hard_grid_using_norvig(self):
        self.gridB='52...6.........7.13...........4..8..6......5...........418.........3..2...87.....'
        grid2=self.norvig.solve(self.gridB)
        gridB_expected=grid2
        self.assertEquals(gridB_expected,grid2)

        

    def test_solve_a_list_grid_using_norvig(self):
        self.gridB="""400000805
                      030000000
                      000700000
                      020000060
                      000080400
                      000010000
                      000603070
                      500200000
                      104000000"""
        grid2=self.norvig.solve(self.gridB)
        expected_grid2= grid2
        self.assertEquals(expected_grid2,grid2)


    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
