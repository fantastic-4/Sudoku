'''
Sudoku Game
'''
from Parser.grid import Grid

from Solver.norvig import Norvig
from Solver.brute import Brute
from Solver.dlx import DLX

from File.config_file_xml import Xmlfile
from File.txt_file import TXTFile

from Main.display import Display 
from File.csv_file import Csvfile


class SudokuGame():
    '''
    CLass to integrate the flow to solve and configure the sudoku game
    '''
    def __init__(self):
        self.grid = Grid()
        self.norvig = Norvig()
        self.brute = Brute()
        self.dlx = DLX()
        self.xml_config_file = Xmlfile("c:\\sudoku\\config\\", "xml_config_file")
        self.display_dic = Display()
        self.file_read = TXTFile("c:\\Sudoku\\", "")
        self.dict_algorithm = {'norvig': self.norvig.solve, \
                               'brute': self.brute.solve, 'dlx': self.dlx.solve}
        
    def solve_sudoku_from_file (self, path, filename):
        '''
        Return dictionary solved with data from a file
        '''
        if (filename[-3:] == 'txt'): 
            self.file_read = TXTFile(path, filename)
            iofile_easy = self.file_read.read_file()
        else:
            self.file_read = Csvfile(path, filename)
            iofile_easy = self.file_read.read_file()
            
        algorithm = self.get_xml_value("default_algorithm").lower()
        self.original = self.grid.set_values(iofile_easy)
        sudoku_resolved = self.dict_algorithm.get(algorithm)(self.original)
        return sudoku_resolved
    
    def solve_sudoku_from_console (self, dictionary):
        '''
        Return dictionary solved with data typed from console
        '''
        algorithm = self.get_xml_value("default_algorithm").lower()
        self.original = dictionary
        sudoku_resolved = self.dict_algorithm.get(algorithm)(dictionary)
        return sudoku_resolved

    def validate_text(self, text):
        '''
        Validate data typed from console to solve the Sudoku
        '''
        while(len(text) < 81): 
            text += "0"
        grid = Grid()
        flag = grid.validate_grid(text)
        if(not flag):
            print("ERROR, Invalid input content.")
        return self.grid.set_values(text), flag
    
    def display(self, dic):
        '''
        Display the Sudoku board
        '''
        print self.display_dic.display(dic)
        
    def export_to_file(self, dic):
        '''
        Export the Sudoku board to file
        '''
        self.file_read.write_file(dic)
        print "\n..........The solution was exported to the file........\n"
        
    def set_xml_value(self, new_value, tag):
        '''
        Update any value of Xml configuration file
        '''
        self.xml_config_file.set_xml_value(new_value, tag)
    
    def get_xml_value(self, tag):
        '''
        Get any value of Xml configuration file
        '''
        return self.xml_config_file.get_xml_value(tag)
    