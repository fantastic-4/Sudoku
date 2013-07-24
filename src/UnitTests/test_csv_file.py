from File.csv_file import Csvfile
import unittest, os, filecmp

class TestCsvFile(unittest.TestCase):
    
    def setUp(self):
        
        self.test_file = None
        
        self.test_file_name = "test-matrix.csv"
        self.file_created = "file_created_for_test.csv"
        
        self.grid_to_solve_with_comma = "042068050,396000208,000000007,\
000750906,005200430,263040780,007000004,059630800,008000573"
        self.grid_to_solve_with_dot_and_comma = "042068050;396000208;\
000000007;000750906;005200430;263040780;007000004;059630800;008000573"
        self.grid_to_solve_with_tab = "042068050\t396000208\t000000007\t\
000750906\t005200430\t263040780\t007000004\t059630800\t008000573"
        
        self.expected_grid_to_solve_parsed = "04206805039600020800000000700075\
0906005200430263040780007000004059630800008000573"
        
        self.expected_grid_solved_with_comma = "742368159,396571248,581492367,\
814753926,975286431,263149785,137825694,459637812,628914573"
        self.expected_grid_solved_with_dot_and_comma = "742368159;396571248;\
581492367;814753926;975286431;263149785;137825694;459637812;628914573"
        self.expected_grid_solved_with_tab = "742368159\t396571248\t581492367\t\
814753926\t975286431\t263149785\t137825694\t459637812\t628914573"
        
        self.dictionary_of_grid_solved = {'H7': '8', 'H9': '2', 'G5': '2', \
'I2': '2', 'I5': '1', 'A3': '2', 'A2': '4', 'A1': '7', 'A7': '1', 'A6': '8', \
'A5': '6', 'A4': '3', 'C5': '9', 'C4': '4', 'C7': '3', 'A8': '5', 'C1': '5', \
'A9': '9', 'C3': '1', 'C2': '8', 'E7': '4', 'E6': '6', 'E5': '8', 'E4': '2', \
'E3': '5', 'E2': '7', 'E1': '9', 'G6': '5', 'G9': '4', 'B2': '9', 'I1': '6', \
'I4': '9', 'I7': '5', 'I6': '4', 'E9': '1', 'B3': '6', 'H8': '1', 'D2': '1', \
'E8': '3', 'B1': '3', 'G1': '1', 'I8': '7', 'G4': '8', 'H6': '7', 'G7': '6', \
'G3': '7', 'D8': '2', 'D9': '6', 'D3': '4', 'G2': '3', 'I9': '3', 'B8': '4', \
'B9': '8', 'B6': '1', 'D1': '8', 'B4': '5', 'B5': '7', 'D4': '7', 'D5': '5', \
'D6': '3', 'D7': '9', 'F2': '6', 'F3': '3', 'F1': '2', 'F6': '9', 'F7': '7', \
'F4': '1', 'F5': '4', 'H4': '6', 'H5': '3', 'B7': '2', 'F9': '5', 'H1': '4', \
'H2': '5', 'H3': '9', 'I3': '8', 'C6': '2', 'G8': '9', 'C9': '7', 'F8': '8',\
'C8': '6'}
        
    def test_if_grid_with_comma_is_parsed_to_be_solved(self):
         
        self.test_file = open(self.test_file_name,"w+")
        self.test_file.write(self.grid_to_solve_with_comma)
        self.test_file.close()
        cf = Csvfile(os.getcwd(),self.test_file_name)
        res = cf.read_file()
         
        self.assertTrue(res == self.expected_grid_to_solve_parsed)
        
    def test_if_grid_with_dot_and_comma_is_parsed_to_be_solved(self):
         
        self.test_file = open(self.test_file_name,"w+")
        self.test_file.write(self.grid_to_solve_with_dot_and_comma)
        self.test_file.close()
        cf = Csvfile(os.getcwd(),self.test_file_name)
        res = cf.read_file()
         
        self.assertTrue(res == self.expected_grid_to_solve_parsed)
        
    def test_if_grid_with_tab_is_parsed_to_be_solved(self):
         
        self.test_file = open(self.test_file_name,"w+")
        self.test_file.write(self.grid_to_solve_with_tab)
        self.test_file.close()
        cf = Csvfile(os.getcwd(),self.test_file_name)
        res = cf.read_file()
         
        self.assertTrue(res == self.expected_grid_to_solve_parsed)
        
    def test_write_file_containing_grid_solved_in_CSV_format_with_comma(self):
        
        self.test_file = open(self.test_file_name,"w+")
        self.test_file.write(self.grid_to_solve_with_comma)
        self.test_file.close()
        cf = Csvfile(os.getcwd(),self.test_file_name)
        cf.read_file()
        
        self.test_file = open(self.test_file_name,"w+")
        self.test_file.write(self.expected_grid_solved_with_comma)
        self.test_file.close()
        
        cf.file_name = self.file_created
        cf.write_file(self.dictionary_of_grid_solved)
        
        self.assertTrue(filecmp.cmp(self.test_file_name, self.file_created))
        os.remove(os.getcwd() + "\\" + self.file_created)
    
    def test_write_file_contains_grid_solved_in_CSV_with_dot_and_comma(self):
        
        self.test_file = open(self.test_file_name,"w+")
        self.test_file.write(self.grid_to_solve_with_dot_and_comma)
        self.test_file.close()
        cf = Csvfile(os.getcwd(),self.test_file_name)
        cf.read_file()
        
        self.test_file = open(self.test_file_name,"w+")
        self.test_file.write(self.expected_grid_solved_with_dot_and_comma)
        self.test_file.close()
        
        cf.file_name = self.file_created
        cf.write_file(self.dictionary_of_grid_solved)
        
        self.assertTrue(filecmp.cmp(self.test_file_name, self.file_created))
        os.remove(os.getcwd() + "\\" + self.file_created)
    
    def test_write_file_containing_grid_solved_in_CSV_format_with_tab(self):
        
        self.test_file = open(self.test_file_name,"w+")
        self.test_file.write(self.grid_to_solve_with_tab)
        self.test_file.close()
        cf = Csvfile(os.getcwd(),self.test_file_name)
        cf.read_file()
        
        self.test_file = open(self.test_file_name,"w+")
        self.test_file.write(self.expected_grid_solved_with_tab)
        self.test_file.close()
        
        cf.file_name = self.file_created
        cf.write_file(self.dictionary_of_grid_solved)
        
        self.assertTrue(filecmp.cmp(self.test_file_name, self.file_created))
        os.remove(os.getcwd() + "\\" + self.file_created)
        
    def tearDown(self):
        os.remove(os.getcwd() + "\\" + self.test_file_name)
        
if __name__ == "__main__":
    unittest.main()