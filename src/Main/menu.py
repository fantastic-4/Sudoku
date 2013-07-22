'''
Sudoku
'''
import os, sys
sys.path.append("../../src")
from Main.sudoku_game import SudokuGame
from Main.solve_console import SolveConsole
from Main.configure_sudoku import ConfigureSudoku

class Menu():
        
    def __init__(self):
        self.Game_console = SudokuGame()
        self.solve = SolveConsole()
        self.configure_settings = ConfigureSudoku()
        self.options = {1: self.solve.solve, 2: self.play_game,\
                         3: self.configure_settings.configure_settings}
    
    def play_game(self):
        print "this is not implemented yet"
    
    def enter_option(self, length,text,error="Incorrect input!. \
    \nPlease enter a proper option."):
        while True:
            num = raw_input(text)
            try:
                num = int(num)
                if (num <= length):
                    return num
                    break
                else:
                    self.error_message(error)
                    pass
            except ValueError:
                self.error_message(error)
                pass
    def error_message(self,text):
        print text
    
    
    def main(self):
        while (True):
            os.system("cls")
            print "============================================"    
            print "    Administration Console for Sudoku Game"
            print "============================================"
            
            print "1: Solve a Sudoku"
            print "2: Play Sudoku"
            print "3: Configure Settings"
            print "4: Exit"
            
            num = self.enter_option(4, "\nPlease enter an option: ")
            
            if (num == 4): 
                print "............Exist.............\n"
                break
            else:
                self.options.get(num)()
            
if __name__ == "__main__":
    main = Menu()
    main.main()