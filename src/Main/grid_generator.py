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
            ran_num = self.validator.digits[self.get_random_integer()]
            if(self.validator.check_lines(ran_num, rand_key, self.values)
               and self.validator.check_square(ran_num, rand_key, self.values)):
                self.values[rand_key] = ran_num
                break
    
    def values_chooser(self, difficulty):
        '''
        Selects items from a grid previously introduced or generated. 
        :param difficulty: Difficulty to choose a range of random selection.
        :return values: return Sudoku grid to be fulfilled as dictionary.
        '''
        numbers_quantity = self.get_hints_quantity(difficulty)
        values_displayed = []
        while numbers_quantity > 0:
            rand_key =  self.get_random_row() + self.get_random_column()  
            if(not rand_key in values_displayed):
                values_displayed.append(rand_key)
                numbers_quantity -= 1
        self.__grid_cleaner(values_displayed)
        return self.values
    
    def get_random_row(self):
        print("--> ", self.validator.rows[self.get_random_integer()])
        return self.validator.rows[self.get_random_integer()]
    
    def get_random_column(self):
        return self.validator.digits[self.get_random_integer()]
    
    def get_random_integer(self):
        '''
        Returns a random number between '0' and '8'
        '''
        return(random.randint(0, 8))
    
    def get_hints_quantity(self, difficulty):
        '''
        Choose a random number of hints according to difficulty provided.
        :param difficulty: Difficulty to choose a range of random selection.
        '''
        if(difficulty == "Easy"):
            return random.randint(30, 35)
        elif(difficulty == "Medium"):
            return random.randint(25, 30)
        else: 
            return random.randint(20, 25)
    
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
