from Solver.solve_algorithm import SolveAlgorithm
from Parser.validator import Validator
import time

class Brute (SolveAlgorithm):
    
    def __init__(self):
        '''Function to set global attributes'''
    
        SolveAlgorithm.__init__(self)
        self.validator = Validator()
        self.dictionary = None
        
        '''Dictionary with Empty Values only'''
        self.empty_values = None
              
        '''List of lists to register moves for each empty cell'''
        self.moves_per_cell = [[]]
    
    def solve(self, dictionary):
        '''Function to initialize global attributes and start the process,
       also calculates the time that takes the algorithm to solve the grid
       Return the grid fulfilled'''
        self.dictionary = dictionary
        self.empty_values = self.__grid_empty_values()
        empties_number = len(self.empty_values.keys())
        while empties_number > 0:
            self.moves_per_cell.append([])
            empties_number -= 1
        
        self.time_elapsed = time.clock()
        self.__start__()
        self.time_elapsed = time.clock() - self.time_elapsed
        
        return self.dictionary
        
    def __grid_empty_values(self):
        '''Function to select all the tuples on dictionary with value as Zero
       Return a dictionary with empty values'''
    
        empties = []
        for key,value in self.dictionary.items():
            if(value == "0" or value == "."):
                empties.append((key,value)) 
        return dict(empties)    
    
    def __start__(self):
        '''Function to start the process of set numbers on cell using 
        Brute Force Algorithm'''
        
        pos = 0
        emp_vals = self.empty_values
        empty_keys = sorted(emp_vals.keys())
        try:
            while pos < len(self.empty_values):
                val = empty_keys[pos]
                if(self.__fill_cell__(pos, val)):
                    pos += 1
                else:
                    self.dictionary[val] = "0"
                    self.moves_per_cell[pos] = []
                    pos -= 1
        except IndexError:
            self.dictionary = False
                    
    def __fill_cell__(self,pos,key):
        '''Function to iterate numbers from 1 to 9 until set a number that 
        can be fit on the cell and return True if a number was set, False
         otherwise'''        
    
        cell_set = False
        for n in range(0,9):
            num = self.validator.digits[n]
            if(self.validator.check_lines(num, key, self.dictionary) and \
               self.validator.check_square(num, key, self.dictionary) 
               and not(num in self.moves_per_cell[pos])):
                cell_set = True
                self.dictionary[key] = num
                self.moves_per_cell[pos].append(num)
                break
        return cell_set