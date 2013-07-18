import unittest
from Parser.grid import Grid
from Solver.dlx import DLX


class TestDlxMatrix(unittest.TestCase):
	def setUp(self):
		self.string='.4398.25.6..425...2....1.949....4..33..6.8...41.2.9..882.5....9....4...253489....'
		self.string_with_points='.4398.25.6..425...2....1.949....4..33..6.8...41.2.9..882.5....9....4...253489....'
		self.string_with_zeros='043980250600425000200001094900004003300608000410209008820500009000040002534890000'
		
		self.rows = [[1, [3,5,6]], [2, [1,4,7]], [3, [2,3,6]],[4, [1,4]], [5, [2,7]], [6, [4,5,7]]]
		self.dlx = DLX()
		self.grid = Grid()
		self.gridA='042068050396000208000000007000750906005200430263040780007000004059630800008000573'
		self.expected_gridA = {'H7': '8', 'H9': '2', 'G5': '2', 'I2': '2', 'I5': '1', 'A3': '2', 'A2': '4', 'A1': '7', 'A7': '1', 'A6': '8', 'A5': '6', 'A4': '3', 'C5': '9', 'C4': '4', 'C7': '3', 'A8': '5', 'C1': '5', 'A9': '9', 'C3': '1', 'C2': '8', 'E7': '4', 'E6': '6', 'E5': '8', 'E4': '2', 'E3': '5', 'E2': '7', 'E1': '9', 'G6': '5', 'G9': '4', 'B2': '9', 'I1': '6', 'I4': '9', 'I7': '5', 'I6': '4', 'E9': '1', 'B3': '6', 'H8': '1', 'D2': '1', 'E8': '3', 'B1': '3', 'G1': '1', 'I8': '7', 'G4': '8', 'H6': '7', 'G7': '6', 'G3': '7', 'D8': '2', 'D9': '6', 'D3': '4', 'G2': '3', 'I9': '3', 'B8': '4', 'B9': '8', 'B6': '1', 'D1': '8', 'B4': '5', 'B5': '7', 'D4': '7', 'D5': '5', 'D6': '3', 'D7': '9', 'F2': '6', 'F3': '3', 'F1': '2', 'F6': '9', 'F7': '7', 'F4': '1', 'F5': '4', 'H4': '6', 'H5': '3', 'B7': '2', 'F9': '5', 'H1': '4', 'H2': '5', 'H3': '9', 'I3': '8', 'C6': '2', 'G8': '9', 'C9': '7', 'F8': '8', 'C8': '6'}
		self.gridB='520006000000000701300000000000400800600000050000000000041800000000030020008700000'
		self.expected_gridB = {'G3': '1', 'F3': '3', 'E8': '5', 'E9': '4', 'C8': '6', 'C9': '2', 'F8': '1', 'F2': '5', 'C4': '9', 'E3': '9', 'C6': '7', 'C7': '5', 'E6': '1', 'C1': '3', 'C2': '1', 'E5': '7', 'D6': '3', 'H7': '9', 'G8': '7', 'F7': '2', 'G1': '9', 'G5': '2', 'I9': '5', 'D3': '2', 'D8': '9', 'A7': '4', 'F5': '9', 'I7': '1', 'I4': '7', 'D2': '7', 'I2': '3', 'I3': '8', 'F4': '6', 'I1': '2', 'A6': '6', 'E2': '8', 'A4': '3', 'A5': '1', 'A2': '2', 'A3': '7', 'C5': '8', 'H9': '8', 'F9': '7', 'A8': '8', 'A9': '9', 'D5': '5', 'D4': '4', 'D7': '8', 'E1': '6', 'D1': '1', 'F6': '8', 'B9': '1', 'B8': '3', 'B7': '7', 'B6': '2', 'B5': '4', 'B4': '5', 'B3': '6', 'B2': '9', 'B1': '8', 'E7': '3', 'E4': '2', 'G6': '5', 'C3': '4', 'G4': '8', 'H8': '2', 'G2': '4', 'F1': '4', 'I8': '4', 'H1': '7', 'H3': '5', 'H2': '6', 'H5': '3', 'G9': '3', 'H4': '1', 'H6': '4', 'D9': '6', 'G7': '6', 'I5': '6', 'A1': '5', 'I6': '9'}
	
	def test_select_movements_on_dlx_matrix_should_display_the_correct_movements(self):
		expected=[4,1,5]
		result=self.dlx.solve_dlx(self.rows)
		self.assertEqual(expected,result)

	def test_convert_a_string_to_a_array_when_it_has_points_should_display_an_array_equivalent_with_zeros(self):
		expected=[0,4,3,9,8,0,2,5,0,6,0,0,4,2,5,0,0,0,2,0,0,0,0,
			1,0,9,4,9,0,0,0,0,4,0,0,3,3,0,0,6,0,8,0,0,0,4,1,0,2,
			0,9,0,0,8,8,2,0,5,0,0,0,0,9,0,0,0,0,4,0,0,0,2,5,3,4,8,9,0,0,0,0]
		result=self.dlx.convert_to_array(self.string_with_points)
		self.assertEqual(expected,result)

	def test_convert_a_string_to_a_array_when_it_has_zeros_should_display_an_array_equivalent_with_zeros(self):
		expected=[0,4,3,9,8,0,2,5,0,6,0,0,4,2,5,0,0,0,2,0,0,0,0,
			1,0,9,4,9,0,0,0,0,4,0,0,3,3,0,0,6,0,8,0,0,0,4,1,0,2,
			0,9,0,0,8,8,2,0,5,0,0,0,0,9,0,0,0,0,4,0,0,0,2,5,3,4,8,9,0,0,0,0]
		result=self.dlx.convert_to_array(self.string_with_zeros)
		self.assertEqual(expected,result)

	def test_convert_a_string_to_a_array_should_display_an_array_equivalent(self):
		
		expected=[0,4,3,9,8,0,2,5,0,6,0,0,4,2,5,0,0,0,2,0,0,0,0,
			1,0,9,4,9,0,0,0,0,4,0,0,3,3,0,0,6,0,8,0,0,0,4,1,0,2,
			0,9,0,0,8,8,2,0,5,0,0,0,0,9,0,0,0,0,4,0,0,0,2,5,3,4,8,9,0,0,0,0]
		result=self.dlx.convert_to_array(self.string)
		self.assertEqual(expected,result)

	def test_solver_sudoku_should_display_the_string_resolved(self):
		result=self.dlx.solve(self.grid.set_values(self.gridA))
		self.assertEqual(self.expected_gridA,result)
		
	def test_if_the_grid_does_not_solution(self):
		var1='700105080008697230206300014362084100001020800084760000090002750005410690040050020'
		result=self.dlx.solve(self.grid.set_values(var1))
		self.assertFalse(result)
		
		
if __name__=='__main__':
	unittest.main()
