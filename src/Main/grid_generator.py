from Parser.grid import Grid
import random
from Parser.validator import Validator
from Solver.norvig import Norvig
from Solver.brute import Brute

class Grid_generator:
    
    def __init__(self):
        
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
            self.__set_random_number__(key)
        brute = Brute()
        self.values = brute.solve(self.values)
        print(self.grid.display(self.values))
        
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
    
    def values_chooser(self, difficulty):
        '''
        Choose a random number of hints according to difficulty provided
        to select them from a grid previously introduced or generated. 
        :param difficulty: to generate a random number of hints between a specific range.
        :return values: return Sudoku grid to be fulfilled as dictionary.
        '''
        if(difficulty == "Easy"): numbers_quantity = random.randint(25,30)
        elif(difficulty == "Medium"): numbers_quantity = random.randint(20,25)
        else: numbers_quantity = random.randint(15,20)
        
        values_displayed = []
        while numbers_quantity > 0:
            rand_key = self.validator.rows[random.randint(0,8)] \
            + self.validator.digits[random.randint(0,8)]
            if(not rand_key in values_displayed):
                values_displayed.append(rand_key)
                numbers_quantity -= 1
                
        self.grid_cleaner(values_displayed)
        return self.values
    
    def __grid_cleaner__(self,values_displayed):
        '''
        Function to clean Grid setting '0' to coordinates that were not selected s hints. 
        :param values_displayed:
        '''
        for row in self.validator.rows:
            for column in self.validator.digits:
                key = row + column
                if(not key in values_displayed): self.values[key] = "0"
        
gg = Grid_generator()
matrix = gg.generate_grid()
gg.values_chooser("Easy")
g = Grid()
print(g.display(matrix))
# a = Norvig()
a = Brute()
# print (g.display(a.__grid_to_dict__(matrix)))
matrixN = a.solve(matrix)
print (g.display(matrixN))