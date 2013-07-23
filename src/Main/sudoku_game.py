from Parser.grid import Grid

from Solver.norvig import Norvig
from Solver.brute import Brute
from Solver.dlx import DLX

from File.config_file_xml import Xmlfile
from File.txt_file import TXTFile

from Main.display import Display 
from File.csv_file import Csvfile


class SudokuGame():
    
    def __init__(self):
        self.grid=Grid()
        self.norvig=Norvig()
        self.brute=Brute()
        self.dlx= DLX()
        self.xml_config_file = Xmlfile('c:\\sudoku\\config\\', 'xml_config_file')
        self.display_dic= Display()
        self.dict_algorithm = {'norvig': self.norvig.solve, \
                               'brute': self.brute.solve, 'dlx': self.dlx.solve}
        
    def solve_sudoku_from_file (self, path, filename):
        if (filename[-3:]== 'txt'): 
            self.file_read=TXTFile(path, filename)
            iofile_easy=self.file_read.read_file()
        else:
            self.file_read=Csvfile(path, filename)
            iofile_easy=self.file_read.read_file()
            
        algorithm = self.get_xml_value("default_algorithm").lower()
        sudoku_resolved=self.dict_algorithm.get(algorithm)\
        (self.grid.set_values(iofile_easy))
        return sudoku_resolved
    
    def solve_sudoku_from_console (self, dictionary):
        algorithm = self.get_xml_value("default_algorithm").lower()
        sudoku_resolved=self.dict_algorithm.get(algorithm)(dictionary)
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
        self.file_read.write_file(dic)
        print "\n..........The solution was exported to the file........\n"
        
    def set_xml_value(self, new_value, tag):
        self.xml_config_file.set_xml_value(new_value, tag)
    
    def get_xml_value(self, tag):
        return self.xml_config_file.get_xml_value(tag)
    