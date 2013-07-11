from Solver.solve_algorithm import Solve_Algorithm
import time

class Brute (Solve_Algorithm):
    
    '''Function to set global attributes'''
    def __init__(self):
        Solve_Algorithm.__init__(self)
        
        '''Var to get the values of the Sudoku grid'''
        self.grid_from_file=("")
        
        '''Values of unsolved grid'''
        self.values = None
        
        '''Dictionary with Empty Values only'''
        self.empty_values = None
              
        '''List of lists to register moves for each empty cell'''
        self.moves_per_cell = None
    
    '''Function to initialize global attributes and start the process,
       also calculates the time that takes the algorithm to solve the grid
       Return the grid fulfilled'''
    def solve(self,grid):
        
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
        
    '''Function to select all the tuples on dictionary with value as Zero
       Return a dictionary with empty values'''
    def __grid_empty_values__(self,grid):
        empties = []
        for key,value in grid.items():
            if(value == '0'or value == '.'):
                empties.append((key,value)) 
        return dict(empties)    
            
    '''Function to validate if the number is already in the square 3x3
       Return True if can be set on the square, False if the number is already on it'''
    def __check_square__(self,num,key):
        flag = True
        ini_row, ini_col = self.__get_ini_row_and_ini_col__(key)
        lim_row = ini_row + 2
        aux = ini_col
        lim_col = ini_col + 2
        while ini_row <= lim_row and flag:
            ini_col = aux
            while ini_col <= lim_col:
                if(self.values[self.grid.rows[ini_row]+str(ini_col)] == num):
                    flag = False
                    break
                ini_col += 1
            ini_row += 1
        return flag
    
    '''Function to validate if the number is already in the row or column
       Return True if can be set on the cell, False if the number is already on row or column'''   
    def __check_lines__(self,num, key):
        flag = True
        row = key[0]
        col = key[1]
        
        for i in range(1,10):
            if(self.values[(row+str(i))] == num):
                flag = False
                break
        if(flag):
            for j in range(0,9):
                if(self.values[self.grid.rows[j]+col] == num):
                    flag = False
                    break
        return flag
    
    '''Function to start the process of set numbers on cell using Brute Force Algorithm'''
    def __start__(self):
        
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
    
    '''Function to iterate numbers from 1 to 9 until set a number that can be fit on the cell
       Return True if a number was set, False otherwise'''        
    def __fill_cell__(self,pos,key):
        cell_set = False
        for n in range(0,9):
            num = self.grid.digits[n]
            if(self.__check_lines__(num, key) and self.__check_square__(num, key) and not(num in self.moves_per_cell[pos])):
                cell_set = True
                self.values[key] = num
                self.moves_per_cell[pos].append(num)
                break
        return cell_set
         
    '''Function to set the top-left coordinate of the square where the number is about to fit
       Return 2 variables, row and column where the square begins'''
    def __get_ini_row_and_ini_col__(self,key):
        
        row = key[0]
        col = key[1]

        if(row=="A" or row=="B" or row=="C"): ini_row = 0
        elif(row=="D" or row=="E" or row=="F"): ini_row = 3
        else: ini_row = 6
            
        if(col=="1" or col=="2" or col=="3"): ini_col = 1
        elif(col=="4" or col=="5" or col=="6"): ini_col = 4
        else: ini_col = 7
        return ini_row,ini_col