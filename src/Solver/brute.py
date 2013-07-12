from Solver.solve_algorithm import Solve_Algorithm
import time

class Brute (Solve_Algorithm):
    
    def __init__(self, grid):
        '''Function to set global attributes'''
    
        Solve_Algorithm.__init__(self, grid)
        
        '''Values of unsolved grid'''
        self.values = None
        
        '''Dictionary with Empty Values only'''
        self.empty_values = None
              
        '''List of lists to register moves for each empty cell'''
        self.moves_per_cell = None
    
    def solve(self,grid):
        '''Function to initialize global attributes and start the process,
       also calculates the time that takes the algorithm to solve the grid
       Return the grid fulfilled'''
        
        '''Here we call to display function, but before that
           we assign to raw_grid var from grid class the value of the input text'''
        self.grid.raw_grid = grid
        self.values = self.grid.set_values(grid)
        self.empty_values = self.__grid_empty_values__(self.values)
        self.moves_per_cell = [[] for i in range(len(self.empty_values.keys()))]
        
        self.time_elapsed = time.clock()
        self.__start__()
        self.time_elapsed = time.clock() - self.time_elapsed
        
        return self.values
        
    def __grid_empty_values__(self,grid):
        '''Function to select all the tuples on dictionary with value as Zero
       Return a dictionary with empty values'''
    
        empties = []
        for key,value in grid.items():
            if(value == '0'or value == '.'):
                empties.append((key,value)) 
        return dict(empties)    
    
    def __start__(self):
        '''Function to start the process of set numbers on cell using Brute Force Algorithm'''
        
        pos = 0
        emp_vals = self.empty_values
        empty_keys = sorted(emp_vals.keys())
        
        while pos < len(self.empty_values):
            val = empty_keys[pos]
            if(self.__fill_cell__(pos, val)):
                pos += 1
            else:
                self.values[val] = "0"
                self.moves_per_cell[pos] = []
                pos -= 1
    
    def __fill_cell__(self,pos,key):
        '''Function to iterate numbers from 1 to 9 until set a number that can be fit on the cell
       Return True if a number was set, False otherwise'''        
    
        cell_set = False
        for n in range(0,9):
            num = self.grid.digits[n]
            if(self.grid.check_lines(num, key, self.values) and self.grid.check_square(num, key, self.values) and not(num in self.moves_per_cell[pos])):
                cell_set = True
                self.values[key] = num
                self.moves_per_cell[pos].append(num)
                break
        return cell_set