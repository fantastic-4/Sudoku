from Main.grid import Grid

from Solver.norvig import Norvig
from Solver.brute import Brute

from File.config_file_xml import Xml_file
from File.txt_file import TXT_File


class SudokuGame():
    
    def __init__(self):
        self.norvig=Norvig()
        self.grid=Grid()
        self.brute=Brute()
        self.xml_config_file = Xml_file('../File/', 'xml_config_file') 
    
    
    def solve_sudoku (self, path, filename):
        txtfile=TXT_File(path, filename)
        iofile_easy=txtfile.read_file()
        
        algorithm = self.xml_config_file.get_xml_value("default_algorithm").lower()
        
        dict_algorithm = {'norvig': self.norvig.solve, 'brute': self.brute.solve}
        sudoku_resolved=dict_algorithm.get(algorithm)(iofile_easy)
        
        return sudoku_resolved, self.xml_config_file
        
        
    def errorMessage(self):
        print "Incorrect input. Please enter a proper option."