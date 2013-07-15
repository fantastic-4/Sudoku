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
        
    
    
    def solve_sudoku (self, path, filename):
        txtfile=TXT_File(path, filename)
        iofile_easy=txtfile.read_file()
        
        xml_config_file = Xml_file('../File/', 'xml_config_file') 
        
        algorithm = xml_config_file.get_xml_value("default_algorithm").lower()
        output = xml_config_file.get_xml_value("solver_output_type").lower()
        
        dict_algorithm = {'norvig': self.norvig.solve(iofile_easy), 'brute': self.brute.solve(iofile_easy)}
        sudoku_resolved=dict_algorithm.get(algorithm, self.errorMessage())
        
            
        print "====================================================="    
        print "The algorithm used to solve is: ", algorithm.upper()
        print "====================================================="
        #print grid.display(sudoku_resolved)
        
        
        if (output == 'console'):
            print self.grid.display(sudoku_resolved)
        if (output == 'file'):
            txtfile.file_name = 'Sudoku_resolved.txt'
            txtfile.output_file(sudoku_resolved)
            print "\n.............The solution was exported to the file.............\n"
        
        return sudoku_resolved
    
    
    def errorMessage(self):
        print "Incorrect input. Please enter a proper option."