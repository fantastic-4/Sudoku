import unittest
from Solver.dlx import DLX


class TestDlxMatrix(unittest.TestCase):
	def setUp(self):
		self.string='.4398.25.6..425...2....1.949....4..33..6.8...41.2.9..882.5....9....4...253489....'
		#self.string='700105080008697230206300014362084100001020800084760000090002750005410690040050020'
		self.string_with_points='.4398.25.6..425...2....1.949....4..33..6.8...41.2.9..882.5....9....4...253489....'
		self.string_with_zeros='043980250600425000200001094900004003300608000410209008820500009000040002534890000'
		
		self.rows = [[1, [3,5,6]], [2, [1,4,7]], [3, [2,3,6]],[4, [1,4]], [5, [2,7]], [6, [4,5,7]]]
		self.sdk = DLX()

	def test_select_movements_on_dlx_matrix_should_display_the_correct_movements(self):
		expected=[4,1,5]
		result=self.sdk.solve(self.rows)
		self.assertEqual(expected,result)

	def test_convert_a_string_to_a_array_when_it_has_points_should_display_an_array_equivalent_with_zeros(self):
		expected=[0,4,3,9,8,0,2,5,0,6,0,0,4,2,5,0,0,0,2,0,0,0,0,
			1,0,9,4,9,0,0,0,0,4,0,0,3,3,0,0,6,0,8,0,0,0,4,1,0,2,
			0,9,0,0,8,8,2,0,5,0,0,0,0,9,0,0,0,0,4,0,0,0,2,5,3,4,8,9,0,0,0,0]
		result=self.sdk.convert_to_array(self.string_with_points)
		self.assertEqual(expected,result)

	def test_convert_a_string_to_a_array_when_it_has_zeros_should_display_an_array_equivalent_with_zeros(self):
		expected=[0,4,3,9,8,0,2,5,0,6,0,0,4,2,5,0,0,0,2,0,0,0,0,
			1,0,9,4,9,0,0,0,0,4,0,0,3,3,0,0,6,0,8,0,0,0,4,1,0,2,
			0,9,0,0,8,8,2,0,5,0,0,0,0,9,0,0,0,0,4,0,0,0,2,5,3,4,8,9,0,0,0,0]
		result=self.sdk.convert_to_array(self.string_with_zeros)
		self.assertEqual(expected,result)

	def test_convert_a_string_to_a_array_should_display_an_array_equivalent(self):
		
		expected=[0,4,3,9,8,0,2,5,0,6,0,0,4,2,5,0,0,0,2,0,0,0,0,
			1,0,9,4,9,0,0,0,0,4,0,0,3,3,0,0,6,0,8,0,0,0,4,1,0,2,
			0,9,0,0,8,8,2,0,5,0,0,0,0,9,0,0,0,0,4,0,0,0,2,5,3,4,8,9,0,0,0,0]
		result=self.sdk.convert_to_array(self.string)
		self.assertEqual(expected,result)

	def test_solver_sudoku_should_display_the_string_solved(self):
		expected='143987256689425317257361894968754123372618945415239678821576439796143582534892761'
		self.sdk.convert_to_array(self.string)
		result=self.sdk.generate_matrix_dlx()
		self.assertEqual(expected,result)
		
if __name__=='__main__':
	unittest.main()
