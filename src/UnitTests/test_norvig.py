import unittest
from Solver.norvig import Norvig
from Parser.grid import Grid
from Main.display import Display
from Solver.solve_algorithm import SolveAlgorithm


class Test_norvig(unittest.TestCase):


    def setUp(self):
        self.grid=Grid()
        self.norvig=Norvig()
        self.display=Display()
        self.sa=SolveAlgorithm()


    def test_solve_a_easy_grid_using_norvig(self):
        gridA='123450600000000000000000000000000000000000000000000000000000000\
000000000000000000' 
        grid2=self.norvig.solve(self.grid.set_values(gridA))
        gridA_expected=grid2
        self.assertEquals(gridA_expected,grid2)
          
           
    
    def test_solve_a_Hard_grid_using_norvig(self):
        gridB='52...6.........7.13...........4..8..6......5...........418......\
...3..2...87.....'
        grid2=self.norvig.solve(self.grid.set_values(gridB))
        gridB_expected=grid2
        self.assertEquals(gridB_expected,grid2)
   
    def test_return_false_if_cannot_solve_the_grid(self):
        gridB='52...6.........7.13......7....4..8..6......5...........418......\
...3..2...87.....'
        grid2=self.norvig.solve(self.grid.set_values(gridB))
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
        gridA='003020600900305001001806400008102900700000008006708200002609500\
800203009005010300'
        self.norvig.solve(self.grid.set_values(gridA))
        self.assertTrue(self.norvig.time_elapsed != 0)
       
    def test_define_solve_method_from_solve_algorithm_raise_message(self):
        gridA='003020600900305001001806400008102900700000008006708200002609500\
800203009005010300'
        self.assertRaises(self.norvig.solve(self.grid.set_values(gridA)))

    def test_solve__algorithm_with_grid_already_solved(self):
        gridA={'I6': '7', 'H9': '9', 'I2': '9', 'E8': '3', 'H3': '4', 'H7': '7'\
, 'I7': '3', 'I4': '4', 'H5': '5', 'F9': '5', 'G7': '5', 'G6': '9', 'G5': '8', \
'E1': '7', 'G3': '2', 'G2': '7', 'G1': '3', 'I1': '6', 'C8': '9', 'I3': '5', \
'E5': '6', 'I5': '1', 'C9': '3', 'G9': '4', 'G8': '1', 'A1': '4', 'A3': '3', \
'A2': '8', 'A5': '2', 'A4': '9', 'A7': '6', 'A6': '1', 'C3': '1', 'C2': '5', \
'C1': '2', 'E6': '4', 'C7': '4', 'C6': '6', 'C5': '7', 'C4': '8', 'I9': '2', \
'D8': '7', 'I8': '8', 'E4': '5', 'D9': '6', 'H8': '6', 'F6': '8', 'A9': '7', \
'G4': '6', 'A8': '5', 'E7': '1', 'E3': '9', 'F1': '1', 'F2': '3', 'F3': '6', \
'F4': '7', 'F5': '9', 'E2': '2', 'F7': '2', 'F8': '4', 'D2': '4', 'H1': '8', \
'H6': '3', 'H2': '1', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '4', 'B6': '5', \
'B7': '8', 'E9': '8', 'B1': '9', 'B2': '6', 'B3': '7', 'D6': '2', 'D7': '9', \
'D4': '1', 'D5': '3', 'B8': '2', 'B9': '1', 'D1': '5'}
        self.assertRaises(self.norvig.solve(self.grid.set_values(gridA)))

    def test_solve_algorithm_solve_method_is_defined(self):
        gridA='003020600900305001001806400008102900700000008006708200002609500\
800203009005010300'
        self.sa.solve(gridA)

        
if __name__ == "__main__":
    unittest.main()
