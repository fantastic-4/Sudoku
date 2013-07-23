import os

from Main.play_sudoku import PlaySudoku
from Main.grid_generator import GridGenerator
from File.txt_file import TXTFile

class PlayConsole:
    
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
                    self.__start(self.__load_game()[0],
                                 self.__load_game()[1])
                elif(option == 3):
                    self.__start(self.__enter_grid(), "00:00")
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
                print(key + ") " + keys_from_files[key])
            print(message)
            try:
                option = int(raw_input("Insert the option number of game saved: "))
                if(option in keys_from_files):
                    self.__load_game(keys_from_files[key])
                else:
                    message = "\nNo option from menu was typed, please try again.\n"
            except ValueError:
                message = "\nWrong option, please try again.\n"
#         self.txtfile.load_Game(self.save_path, file_name)
    
    def __load_game(self,file_name):
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
        for f in files:
            if(counter < self.maximum_files_displayed):
                dict_of_files[counter] = f
                counter += 1
            else: break
        return dict_of_files
    
    def __enter_grid(self):
        '''
        Read a Sudoku grid entered from console
        '''
        os.system("cls")
        print "====================================================="    
        print "\t\tInput Sudoku Grid instructions"
        print "=====================================================\n"
        print("1) Enter 81 numbers and press Enter key.")
        print("2) Use '0' or '.' to make reference to empty slots.")
        print("3) Press Enter key, to fill the rest with empty slots")
        print("4) Only numbers are allowed")
        print("5) To exit this option press Q key\n")
        
        flag = False
        while not flag:
            input_text = raw_input("Start to enter numbers: ")
            if(input_text in "qQ"):
                flag = False
                break
            input_text, flag = self.game.validate_text(input_text)
            
        if(flag):
            return (input_text)
            
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
            elif(command.upper() == "SOLVE"): message = self.play.play(command)+\
"\n\nType 'EXIT' to back to menu."
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