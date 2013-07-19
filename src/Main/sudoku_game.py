from Parser.grid import Grid

from Solver.norvig import Norvig
from Solver.brute import Brute

from File.config_file_xml import Xml_file
from File.txt_file import TXT_File

from Main.display import Display 

class SudokuGame():
    
    def __init__(self):
        self.norvig=Norvig()
        self.grid=Grid()
        self.brute=Brute()
        self.xml_config_file = Xml_file('../File/', 'xml_config_file')
        self.display_dic= Display()
        
    
    
    def solve_sudoku_from_file (self, path, filename):
        self.txtfile=TXT_File(path, filename)
        iofile_easy=self.txtfile.read_file()
        
        algorithm = self.xml_config_file.get_xml_value("default_algorithm").lower()
        dict_algorithm = {'norvig': self.norvig.solve, 'brute': self.brute.solve}
        sudoku_resolved=dict_algorithm.get(algorithm)(self.grid.set_values(iofile_easy))
        return sudoku_resolved
    
    def solve_sudoku_from_console (self, dictionary):
        algorithm = self.xml_config_file.get_xml_value("default_algorithm").lower()
        dict_algorithm = {'norvig': self.norvig.solve, 'brute': self.brute.solve}
        sudoku_resolved=dict_algorithm.get(algorithm)(dictionary)
        return sudoku_resolved

    def validate_text(self, text):
        while(len(text) < 81): text += "0"
        grid = Grid()
        flag = grid.validate_grid(text)
        if(not flag):
            print("ERROR, Invalid input content.")
        return self.grid.set_values(text),flag
    
    def display(self, dic):
        print self.display_dic.display(dic)
        
    def export_to_file(self, dic):
        self.txtfile.write_file(dic)
        print "\n.............The solution was exported to the file.............\n"
        
    def set_xml_value(self, new_value, tag):
        self.xml_config_file.set_xml_value(new_value, tag)
    
    def get_xml_value(self, tag):
        return self.xml_config_file.get_xml_value(tag)
    