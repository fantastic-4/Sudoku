
from File.csvfile import CsvFile
class TestCsvFile:
    
    def __init__(self):
        
        self.cf = CsvFile()
        self.grid_one_row_separate_elements = "0,4,2,0,6,8,0,5,0,3,9,6,0,0,0,2,0,8,0,0,0,0,0,0,0,0,7,0,0,0,7,5,0,9,0,6,0,0,5,2,0,0,4,3,0,2,6,3,0,4,0,7,8,0,0,0,7,0,0,0,0,0,4,0,5,9,6,3,0,8,0,0,0,0,8,0,0,0,5,7,3"
        self.grid_nine_rows_separate_elements = '''0,4,2,0,6,8,0,5,0
                                                   3,9,6,0,0,0,2,0,8
                                                   0,0,0,0,0,0,0,0,7
                                                   0,0,0,7,5,0,9,0,6
                                                   0,0,5,2,0,0,4,3,0
                                                   2,6,3,0,4,0,7,8,0
                                                   0,0,7,0,0,0,0,0,4
                                                   0,5,9,6,3,0,8,0,0
                                                   0,0,8,0,0,0,5,7,3'''
        self.expected_grid = ".42.68.5.396...2.8........7...75.9.6..52..43.263.4.78...7.....4.5963.8....8...573"
        
    def test_grid_one_row_separate_elements(self):
        file = open(self.grid_one_row_separate_elements,"r")
        self.cf.file = file
        line = self.cf.read_file()
        
        #self.
        "test_matrix.csv"