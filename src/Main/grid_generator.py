'''
Sudoku Game
'''
from Parser.grid import Grid
import random
from Parser.validator import Validator
from Solver.brute import Brute

class GridGenerator:
    '''
    Generator Sudoku dictionary
    '''
    def __init__(self):
        '''
        '''
        self.grid = Grid()
        self.validator = Validator()
        self.values = None
        
    def generate_grid(self):
        '''
        Function to generate a Sudoku grid ready to be fulfilled
        '''
        empty_grid_text = "0" * 81
        self.values = self.grid.set_values(empty_grid_text)
        
        for column in self.validator.digits:
            key = "A" + column
            self.__set_random_number(key)
        brute = Brute()
        self.values = brute.solve(self.values)
        
        return self.values
                    
    def __set_random_number(self, rand_key):
        '''
        Function to set a random number on a specific cell.
        :param rand_key:
        '''
        while True:
            ran_num = self.validator.digits[random.randint(0, 8)]
            if(self.validator.check_lines(ran_num, rand_key, self.values)
               and self.validator.check_square(ran_num, rand_key, self.values)):
                self.values[rand_key] = ran_num
                break
    
    def values_chooser(self, difficulty):
        '''
        Choose a random number of hints according to difficulty provided
        to select them from a grid previously introduced or generated. 
        :param difficulty: to generate a random number of hints between a 
        specific range.
        :return values: return Sudoku grid to be fulfilled as dictionary.
        '''
        if(difficulty == "Easy"):
            numbers_quantity = random.randint(30, 35)
        elif(difficulty == "Medium"):
            numbers_quantity = random.randint(25, 30)
        else: 
            numbers_quantity = random.randint(20, 25)
        
        values_displayed = []
        while numbers_quantity > 0:
            rand_key = self.validator.rows[random.randint(0, 8)] \
            + self.validator.digits[random.randint(0, 8)]
            if(not rand_key in values_displayed):
                values_displayed.append(rand_key)
                numbers_quantity -= 1
                
        self.__grid_cleaner(values_displayed)
        return self.values
    
    def __grid_cleaner(self, values_displayed):
        '''
        Function to clean Grid setting '0' to coordinates that were not selected s hints. 
        :param values_displayed:
        '''
        for row in self.validator.rows:
            for column in self.validator.digits:
                key = row + column
                if(not key in values_displayed): 
                    self.values[key] = "0"
