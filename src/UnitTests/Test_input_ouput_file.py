import unittest
import os.path
from File.input_output_file import IO_File


class TestIO_file(unittest.TestCase):
    """Unit Tests"""

    def setUp(self):
        self.file = IO_File("To_read_sudoku.txt")
    
#     def test_import_file (self):
#         import_sudoku_file= self.file.input_file('========')
#         r = open("To_read_sudoku.txt", 'r')
#         contents = r.read().split('========')
#         self.assertEquals(import_sudoku_file, contents)
         
    def test_export_file_exist (self):
        values = {'I6': '0', 'H9': '9', 'I2': '0', 'E8': '0', 'H3': '0', 'H7': '0', 'I7': '3', 'I4': '0', 'H5': '0', 'F9': '0', 'G7': '5', 'G6': '9', 'G5': '0', 'E1': '7', 'G3': '2', 'G2': '0', 'G1': '0', 'I1': '0', 'C8': '0', 'I3': '5', 'E5': '0', 'I5': '1', 'C9': '0', 'G9': '0', 'G8': '0', 'A1': '0', 'A3': '3', 'A2': '0', 'A5': '2', 'A4': '0', 'A7': '6', 'A6': '0', 'C3': '1', 'C2': '0', 'C1': '0', 'E6': '0', 'C7': '4', 'C6': '6', 'C5': '0', 'C4': '8', 'I9': '0', 'D8': '0', 'I8': '0', 'E4': '0', 'D9': '0', 'H8': '0', 'F6': '8', 'A9': '0', 'G4': '6', 'A8': '0', 'E7': '0', 'E3': '0', 'F1': '0', 'F2': '0', 'F3': '6', 'F4': '7', 'F5': '0', 'E2': '0', 'F7': '2', 'F8': '0', 'D2': '0', 'H1': '8', 'H6': '3', 'H2': '0', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '0', 'B6': '5', 'B7': '0', 'E9': '8', 'B1': '9', 'B2': '0', 'B3': '0', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '0', 'B8': '0', 'B9': '1', 'D1': '0'}
        self.file.output_file(values)
        self.assertTrue(os.path.exists('Sudoku_Exported.txt'))
        
    
        
        

if __name__ == '__main__':
    unittest.main()