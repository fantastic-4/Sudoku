from Parser.grid import Grid
import random
from Parser.validator import Validator
from Solver.norvig import Norvig
class Grid_generator:
    
    def __init__(self):
        
        self.grid = Grid()
        self.validator = Validator()
        self.values = None
        
    def generate_grid(self, difficulty):
        '''
        Function to generate a Sudoku grid ready to be fulfilled
        :param difficulty: the level for the game
        '''
        
        empty_grid_text = "0" * 81
        self.values = self.grid.set_values(empty_grid_text)
        
        if(difficulty == "Easy"): numbers_quantity = random.randint(35,40)
        elif(difficulty == "Medium"): numbers_quantity = random.randint(20,25)
        else: numbers_quantity = random.randint(15,20)
        
        while numbers_quantity > 0:
            rand_key = self.validator.rows[random.randint(0,8)] + self.validator.digits[random.randint(0,8)]
            
            if(self.values[rand_key] == "0"):
                self.__set_random_number__(rand_key)
                numbers_quantity -= 1
        
        return self.values
            
    def __set_random_number__(self, rand_key):
        '''
        Function to set a random number on a specific cell.
        :param rand_key:
        '''
        while True:
            rand_num = self.validator.digits[random.randint(0,8)]
            if(self.validator.check_lines(rand_num, rand_key, self.values)
               and self.validator.check_square(rand_num, rand_key, self.values)):
                self.values[rand_key] = rand_num
                break