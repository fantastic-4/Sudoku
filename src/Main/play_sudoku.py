from Parser.validator import Validator
from Solver.norvig import Norvig
from Solver.brute import Brute
from Solver.dlx import DLX
import time
from File.txt_file import TXTFile

class PlaySudoku:
    
    def __init__(self, dictionary, algorithm, save_path):
        
        self.validator = Validator()
        self.dictionary = dictionary
        self.initial_state = dictionary
        self.algorithm = algorithm
        self.empties = self.__grid_empty_values([])
        
        self.norvig = Norvig()
        self.brute = Brute()
        self.dlx = DLX()
        
        self.squares = [a+b for a in self.validator.rows for b in self.validator.digits]
        self.time_elapsed = 0
        self.start_time = time.clock()
        self.initial_time = "00:00"
        self.path = save_path
        self.file_name = ""
        self.moves_played = []
    
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
    
    def __grid_empty_values(self,empty_grid):
        '''
        Function to select all the tuples on dictionary with value as Zero
        '''
        for key,value in self.dictionary.items():
            if(value == "0" or value == "."):
                empty_grid.append((key,value))
        return dict(empty_grid)
    
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
    
    def __reset_game(self):
        '''
        Function to load a game from a previous saved game.
        :param dictionary: Dictionary from saved game.
        '''
        self.time_elapsed = 0
        self.start_time = time.clock()
        self.set_start_time(self.initial_time)
        self.dictionary = self.initial_state
        self.empties = self.__grid_empty_values([])
    
    def __solve(self, dict_to_solve):
        '''
        Function to Solve the current grid using the default algorithm
        '''
        if(self.algorithm == "Norvig"): dict_solved = self.norvig.solve(dict_to_solve)
        elif(self.algorithm == "Brute"): dict_solved = self.brute.solve(dict_to_solve)
        else: dict_solved = self.dlx.solve(dict_to_solve)
        return (dict_solved)
        
    def __calculate_time(self,parsed_time):
        minutes,seconds = parsed_time.split(":")
        return ((int(minutes)*60) + int(seconds))
        
    def get_time(self):
        '''
        Function to retrieve the time elapsed so far
        '''
        self.time_elapsed += (time.clock() - self.start_time)
        minutes = 0
        while self.time_elapsed >= 60:
            minutes += 1
            self.time_elapsed -= 60
        return (str(minutes) + ":" + "{0:.5f}".format(self.time_elapsed))
    
    def set_start_time(self,new_time):
        '''
        Function to set the time where the clock will start to run.
        :param time: Time to start to run the clock.
        '''
        self.initial_time = new_time
        minutes,seconds = new_time.split(":")
        self.time_elapsed = (int(minutes)*60) + int(seconds)
    
    def __save(self):
        '''
        Function to save current game with the current time elapsed.
        '''
        file_to_save = TXTFile(self.path,self.file_name)
        file_to_save.save_game(self.dictionary, self.get_time())
        return ("The grid was saved")
    
    def __hint(self):
        '''
        Function to get a hint with the minor number of possibilities.
        '''
        if(self.norvig.solve(self.dictionary) != False):
            current_values = self.norvig.grid_to_dict(self.dictionary)
            current_empties = self.__grid_empty_values([])
            if(len(current_empties)>0):
                len_poss = 10
                for pos in current_values.keys():
                    if (pos in current_empties.keys()
                        and len(current_values[pos]) < len_poss):
                        len_poss = len(current_values[pos])
                        min_pos = pos
                hint = self.__calculate_hint(current_values, len_poss, min_pos)
                return ("Hint: " + min_pos + ":" + hint)
            else: return ("No hints to give.")
        else: return ("ERROR, Current Grid has no Solution")
        
    def __calculate_hint(self,current_values, len_poss, min_pos):
        '''
        Function to calculate the hint according to parameters given.
        :param current_values: Current values in the grid.
        :param len_poss: Minor length of possibilities 
        :param min_pos: Position where the minor possibilities are.
        '''
        if(len_poss > 1):
            len_poss -=1
            aux = self.dictionary
            aux[min_pos] = current_values[min_pos][len_poss]
            while(self.__solve(aux) == False):
                len_poss -= 1
                aux = self.dictionary
                aux[min_pos] = current_values[min_pos][len_poss]
            hint = len_poss
        else: hint = len_poss - 1
        return (current_values[min_pos][hint])
            
    def __undo(self):
        '''
        Function to undo moves played before.
        '''
        if(len(self.moves_played)>0):
            key = self.moves_played.pop()
            self.dictionary[key] = "0"
            return ("Last move was: " + key)
        else:
            return("No moves were made.")
       
    def __last_good_square(self):
        '''
        Function to return to last solvable game.
        '''
        if(self.norvig.solve(self.dictionary) != False):
            while(len(self.moves_played)>0):
                if(not self.__verify_game()):
                    self.__undo()
                else: break
            else: return ("Game returned to last good game.")
        else: return ("ERROR, Current Grid has no Solution")
         
    def play(self,command):
        '''
        Function to read a command given and perform a method
        according to that command.
        :param command: command to be executed.
        '''
        if(":" in command):
            key,num = command.upper().split(":")
            if(num.upper() == "HINT"):
                message = "Hint: " + key + ":" + self.__get_hint(key)
            elif(self.__play_move(key, num)):
                message = "Number: " + num + " was added to: " + key
            else: message = "ERROR, Wrong Square"
        else:
            if(command.upper() == "VERIFY"): 
                if(self.__verify_game()):
                    message = "Congratulations, You solved the Grid!!"
                else:
                    message = "ERROR, The grid is not fulfilled as expected."
            elif(command.upper() == "SOLVE"):
                if(self.__solve(self.dictionary) != False):
                    message = "The grid was solved"
                else: message = "Current grid cannot be solved."
            elif(command.upper() == "SAVE"): message = self.__save()
            elif(command.upper() == "HINT"): message = self.__hint()
            elif(command.upper() == "RESET"): 
                self.__reset_game()
                message = "The game was reset to initial state."
            elif(command.upper() == "UNDO"): message = self.__undo()
            elif(command.upper() == "RETURN"): message = self.__last_good_square()
            else: message = "ERROR, command not valid."
        return message