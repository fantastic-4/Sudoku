from Parser.validator import Validator
from Solver.norvig import Norvig
from Solver.brute import Brute
import time
from File.txt_file import TXT_File

class Play_sudoku:
    
    def __init__(self, dictionary, algorithm):
        
        self.validator = Validator()
        self.dictionary = dictionary
        self.algorithm = algorithm
        self.empties = []
        self.__grid_empty_values()
        
        self.norvig = Norvig()
        self.brute = Brute()
        
        self.squares = [a+b for a in self.validator.rows for b in self.validator.digits]
        self.time_elapsed = 0
        self.start_time = time.clock()
        
        self.path = "C:\sudoku\save"
        self.file_name = ""
    
    def __play_move(self, key, num):
        '''
        Function to add numbers to the grid as move played.
        :param key: position to insert a number
        :param num: number to insert in a specific position
        :return boolean: True if the number was added in a empty slot,
        False otherwise.
        '''
        if(key in self.squares and key in self.empties):
            self.dictionary[key] = num
            return True
        else: return False
    
    def __grid_empty_values(self):
        '''
        Function to select all the tuples on dictionary with value as Zero
        '''
    
        for key,value in self.dictionary.items():
            if(value == "0" or value == "."):
                self.empties.append((key,value))
        self.empties = dict(self.empties)
    
    def __get_hint(self,key):
        '''
        Function to get possible numbers in a specific position.
        :param key: Position to provide for hints. 
        '''
        current_values = self.norvig.grid_to_dict(self.dictionary)
        return current_values[key]
    
    def __verify_game(self):
        '''
        Function to validate if the current grid is valid.
        '''
        for square in self.squares:
            if(not self.validator.check_lines(self.dictionary[square], square, self.dictionary)
               or not self.validator.check_square(self.dictionary[square], square, self.dictionary)
               or self.dictionary[square] in "0."):
                return False
        return True
    
    def __load_game(self, dictionary):
        '''
        Function to load a game from a previous saved game.
        :param dictionary: Dictionary from saved game.
        '''
        self.dictionary = dictionary
        self.__grid_empty_values()
    
    def __solve(self):
        '''
        Function to Solve the current grid using the default algorithm
        '''
        dict_algorithm = {"norvig": self.norvig.solve, "brute": self.brute.solve}
        dict_solved = dict_algorithm.get(self.algorithm)(self.dictionary)
        
        return (dict_solved)
        
    def __get_time(self):
        '''
        Function to retrieve the time elapsed so far
        '''
        self.time_elapsed += (time.clock() - self.start_time)
        minutes = 0
        while self.time_elapsed >= 60:
            minutes += 1
            self.time_elapsed -= 60
        return (str(minutes) + ":" + str(self.time_elapsed))
    
    def set_start_time(self,new_time):
        '''
        Function to set the time where the clock will start to run.
        :param time: Time to start to run the clock.
        '''
        minutes,seconds = new_time.split(":")
        self.time_elapsed = (int(minutes)*60) + int(seconds)
    
    def __save(self):
        file_to_save = TXT_File(self.path,self.file_name)
        file_to_save.save_game(self.dictionary, self.__get_time())
        return ("The grid was saved")
        
    def play(self,command):
        message = ""
        if(":" in command):
            key,num = command.split(":")
            if(num.upper() == "HINT"): message = "Hint for: " + key + " -> " + self.__get_hint(key)
            elif(self.__play_move(key, num)): message = "Number: " + num + "was added to: " + key
            else: message = "ERROR, Wrong Coordinate"
        else:
            if(command.upper() == "VERIFY"): 
                if(self.__verify_game()): message = "Congratulations, the You solved the Grid!!"
                else: message = "ERROR, The grid is not fulfilled as expected."
            elif(command.upper() == "SOLVE"):
                if(self.__solve() != False): message = "The grid was solved"
                else: message = "Current grid cannot be solved."
            elif(command.upper() == "TIME"): message = "Time elapsed: " + self.__get_time()
            elif(command.upper() == "SAVE"): message = self.__save()
                
        return message