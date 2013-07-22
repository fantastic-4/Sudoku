from Console.play_sudoku import PlaySudoku
from Main.grid_generator import GridGenerator
from Main.sudoku_game import SudokuGame
import sys

sys.path.append("../../src")

class PlayInterface:
    
    def __init__(self):
 
        self.game = SudokuGame()
        self.difficulty = self.game.get_xml_value("difficulty_level")
        self.algorithm = self.game.get_xml_value("default_algorithm")
        self.save_path = self.game.get_xml_value("save_game")
        
        self.generator = GridGenerator()
        self.play = None
    
    def display_menu(self):
        '''
        Function to display menu and load specific functions.
        '''
        while True:
            print("***** Play Sudoku *****\n")
            print("1) Generate random Sudoku grid.")
            print("2) Load Sudoku game from file.")
            print("3) Enter a grid manually.")
            print("4) Back")
            try:
                option = int(raw_input("Enter a option number: "))
                if(option == 1): self.__start(self.__new_game())
                elif(option == 2): self.__start(self.__load_game())
                elif(option == 3): self.__start(self.__enter_grid())
                elif(option == 4): break
                else: print("No option from menu was entered, please try again.\n")
            except ValueError:
                print("Wrong option, please try again.\n")
    
    def __new_game(self):
        '''
        Function to retrieve a generated grid.
        :Return: Dictionary generateed.
        '''
        self.generator.generate_grid()
        return(self.generator.values_chooser(self.difficulty))
        
    def __load_game(self):
        pass
    
    def __enter_grid(self):
        '''
        Read a Sudoku grid entered from console
        '''
        print "====================================================="    
        print "Input Sudoku Grid instructions"
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
            dictionary = input_text
            return (dictionary)
            
    def __start(self, dictionary):
        '''
        Function to start the game.
        :param dictionary: dictionary to solve the grid.
        '''
        while True:
            print("***** Commands to Play Sudoku *****\n")
            print("a) To insert a number into Sudoku grid,\n\
            type the coordinate and the number separated by ':'.\n\
            Example: A3:1")
            print("b) For an specific hint type the coordinate and 'hint'\
            separated by ':'.\n\
            Example: A3:hint")
            print("c) For a random hint just type: 'hint'")
            print("d) To solve the current grid type: 'solve'")
            print("e) To validate the current grid, type: 'validate'")
            print("f) To save the game, type: 'save'")
            print("g) To exit of the game type: 'exit'\n")
            self.play = PlaySudoku(dictionary, self.algorithm, self.save_path)
            print("\nDifficulty: " + self.difficulty +
                  "\nTime elapsed: " + self.play.get_time() + "\n")
            self.game.display(self.play.dictionary)
            command = raw_input("Enter a command: ")
            if(command.upper() == "EXIT"): break
            else: print(self.play.play(command))
        
pi = PlayInterface()
pi.display_menu()