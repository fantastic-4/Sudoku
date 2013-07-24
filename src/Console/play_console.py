'''
Submenu to play Sudoku 
'''
import os

from Main.play_sudoku import PlaySudoku
from Main.grid_generator import GridGenerator
from File.txt_file import TXTFile

class PlayConsole:
    '''
    Play a Sudoku game from console
    '''
    def __init__(self, sudoku):
 
        self.game = sudoku
        self.difficulty = self.game.get_xml_value("difficulty_level")
        self.algorithm = self.game.get_xml_value("default_algorithm")
        self.save_path = self.game.get_xml_value("save_game")
        self.maximum_files_displayed = self.game.get_xml_value("save_game_number")
        
        self.generator = GridGenerator()
        self.play = None
        self.txtfile = TXTFile("", "")
    
    def display_menu(self):
        '''
        Function to display menu and load specific functions.
        '''
        message = ""
        while True:
            os.system("cls")
            print "====================================================="
            print("\t\tPlay Sudoku")
            print "=====================================================\n"
            print("1) Generate random Sudoku grid.")
            print("2) Load Sudoku game from file.")
            print("3) Enter a grid manually.")
            print("4) Back")
            print(message)
            try:
                option = int(raw_input("Enter a option number: "))
                if(option == 1):
                    self.__start(self.__new_game(), "00:00")
                elif(option == 2):
                    grid, time_elapsed = self.__choose_saved_games()
                    self.__start(grid, time_elapsed)
                elif(option == 3):
                    result = self.__enter_grid()
                    if(result == None): break
                    self.__start(result, "00:00")
                elif(option == 4):
                    break
                else: message = "\nNo option from menu was typed, please try again.\n"
            except ValueError:
                message = "\nWrong option, please try again.\n"
    
    def __new_game(self):
        '''
        Function to retrieve a generated grid.
        :Return: Dictionary generated.
        '''
        self.generator.generate_grid()
        dictionary = self.generator.values_chooser(self.difficulty)
        return(dictionary)
        
    def __choose_saved_games(self):
        '''
        Function to load game from file.
        '''
        files_to_open = self.__get_saved_files()
        keys_from_files = files_to_open.keys()
        message = ""
        while True:
            os.system("cls")
            print "====================================================="    
            print "\t\tSaved Games"
            print "=====================================================\n"
            for key in keys_from_files:
                print(str(key) + ") " + files_to_open[key])
            print(message)
            try:
                option = int(raw_input("Insert the option number of game saved: "))
                if(option in keys_from_files):
                    grid, time_elapsed = self.__load_game(files_to_open[key])
                    return(grid, time_elapsed)
                else:
                    message = "\nNo option from menu was typed, please try again.\n"
            except ValueError:
                message = "\nWrong option, please try again.\n"
#         self.txtfile.load_Game(self.save_path, file_name)
    
    def __load_game(self, file_name):
        '''
        Function to load game.
        :param file_name: name of the file to be loaded.
        '''
        grid, time_elapsed = self.txtfile.load_Game(self.save_path,
                                                    file_name)
        
        return(self.game.grid.set_values(grid), time_elapsed)
        
    def __get_saved_files(self):
        '''
        Function to display the list of the saved games files.
        '''
        files = os.listdir(self.save_path)
        dict_of_files = {}
        counter = 1
        for file_read in files:
            if(counter < self.maximum_files_displayed):
                dict_of_files[counter] = file_read
                counter += 1
            else: break
        return dict_of_files
    
    def __enter_grid(self):
        '''
        Read a Sudoku grid entered from console
        '''
        message = ""
        flag = False
        while not flag:
            os.system("cls")
            print "====================================================="    
            print "\t\tInput Sudoku Grid instructions"
            print "=====================================================\n"
            print("- Enter 81 numbers and press Enter key.")
            print("- Use '0' or '.' to make reference to empty slots.")
            print("- Press Enter key, to fill the rest with empty slots")
            print("- Only numbers are allowed")
            print("- To exit this option press 'Q' or just 'Enter' key.\n")
            print(message)
            input_text = raw_input("Start to enter numbers: ")
            if(input_text in "qQ"):
                flag = False
                break
            input_text, flag = self.game.validate_text(input_text)
            if(flag):
                return (input_text)
            else: message = "\nERROR, wrong grid and/or option, please try again.\n"
            
    def __start(self, dictionary, start_time):
        '''
        Function to start the game.
        :param dictionary: dictionary to solve the grid.
        '''
        self.play = PlaySudoku(self.game, dictionary, self.algorithm, self.save_path)
        self.play.set_elapsed_time(start_time)
        message = ""
        while True:
            self.__display_commands()
            self.__display_board()
            print(message + "\n\n")
            command = raw_input("Enter a command: ")
            if(command.upper() == "EXIT"): break
            elif(command.upper() == "SOLVE"):
                message = self.play.play(command)+ "\n\nType 'EXIT' to back to menu."
            else: message = self.play.play(command)

    def __display_commands(self):
        '''
        Function to display the commands to use in game.
        '''
        os.system("cls")
        print "====================================================="
        print("\t\tCommands to Play Sudoku")
        print "=====================================================\n"
        print("<Coordinate>:<number>\t: To insert a number into Sudoku grid.\
                \n\t\t\t  Example: 'A3:1'")
        print("'hint'\t\t\t: For an specific or random hint.\
                \n\t\t\t  Example: 'A3:hint', 'hint'\n")
        print("'solve'\t\t\t: To solve the current grid.")
        print("'validate'\t\t: To validate the current grid.")
        print("'save'\t\t\t: To save the game.")
        print("'undo'\t\t\t: To back to last move played")
        print("'reset'\t\t\t: To reset the current game to initial state.")
        print("'return'\t\t: To back to last move where the grid was solvable.")
        print("'exit'\t\t\t: To exit of the game.\n")
        
    def __display_board(self):
        '''
        Function to display the current grid.
        '''
        print("\nDifficulty: " + self.difficulty +
                  "\nTime elapsed: " + self.play.get_time() + "\n")
        self.game.display(self.play.dictionary)