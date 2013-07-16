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
    
    
    def solve_sudoku_from_file (self, path, filename):
        txtfile=TXT_File(path, filename)
        iofile_easy=txtfile.read_file()
        
        algorithm = self.xml_config_file.get_xml_value("default_algorithm").lower()
        dict_algorithm = {'norvig': self.norvig.solve, 'brute': self.brute.solve}
        sudoku_resolved=dict_algorithm.get(algorithm)(iofile_easy)
        
        return sudoku_resolved
    
    def solve_sudoku_from_console (self, string):
        pass
        #algorithm = self.xml_config_file.get_xml_value("default_algorithm").lower()
        #dict_algorithm = {'norvig': self.norvig.solve, 'brute': self.brute.solve}
        #sudoku_resolved=dict_algorithm.get(algorithm)(dictionary)
        
        #return sudoku_resolved
    
    def set_xml_value(self, new_value, tag):
        self.xml_config_file.set_xml_value(new_value,tag)
    
    def get_xml_value(self, tag):
        return self.xml_config_file.get_xml_value(tag)
        
    def errorMessage(self):
        print "Incorrect input. Please enter a proper option."