'''
Sudoku
'''
import os, sys
sys.path.append("../../src")
from Main.sudoku_game import SudokuGame
from Console.solve_console import SolveConsole
from Console.configure_sudoku import ConfigureSudoku

class Menu():
        
    def __init__(self):
        self.game = SudokuGame()
        self.solve = SolveConsole(self.game)
        self.configure_settings = ConfigureSudoku(self.game)
        self.options = {1: self.solve.solve, 2: self.play_game,\
                         3: self.configure_settings.configure_settings}
    
    def play_game(self):
        print "this is not implemented yet"
    
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
            
            num = self.solve.enter_option(4, "\nPlease enter an option: ")
            
            if (num == 4): 
                print "............Exist.............\n"
                break
            else:
                self.options.get(num)()
            
if __name__ == "__main__":
    main = Menu()
    main.main()