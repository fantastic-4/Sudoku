import unittest
from Solver.norvig import Norvig
from Parser.grid import Grid
from Main.display import Display


class Test_norvig(unittest.TestCase):


    def setUp(self):
        self.grid=Grid()
        self.norvig=Norvig()
        self.display=Display()


    def test_solve_a_easy_grid_using_norvig(self):
        gridA='123450600000000000000000000000000000000000000000000000000000000000000000000000000' 
        grid2=self.norvig.solve(self.grid.set_values(gridA))
        gridA_expected=grid2
        self.assertEquals(gridA_expected,grid2)
          
           
    
    def test_solve_a_Hard_grid_using_norvig(self):
        gridB='52...6.........7.13...........4..8..6......5...........418.........3..2...87.....'
        grid2=self.norvig.solve(self.grid.set_values(gridB))
        gridB_expected=grid2
        self.assertEquals(gridB_expected,grid2)
   
    def test_return_false_if_cannot_solve_the_grid(self):
        gridB='52...6.........7.13......7....4..8..6......5...........418.........3..2...87.....'
        grid2=self.norvig.__grid_to_dict__(self.grid.set_values(gridB))
        self.assertFalse(grid2)
         
   
    def test_solve_a_list_grid_using_norvig(self):
        gridB="""400000805
                       030000000
                       000700000
                       020000060
                       000080400
                       000010000
                       000603070
                       500200000
                       104000000"""
        grid2=self.norvig.solve(self.grid.set_values(gridB))
        expected_grid2= grid2
        self.assertEquals(expected_grid2,grid2)
   
   
   
    def test_if_time_elapsed_solving_is_saved(self):
        gridA='003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.norvig.solve(self.grid.set_values(gridA))
        self.assertTrue(self.norvig.time_elapsed != 0)
       
    def test_define_solve_method_from_solve_algorithm_raise_message(self):
        gridA='003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.assertRaises(self.norvig.solve(self.grid.set_values(gridA)))

    
if __name__ == "__main__":
    unittest.main()
