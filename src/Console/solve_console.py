'''
Created on Jul, 2013

'''
import os
from Main.sudoku_game import SudokuGame

class SolveConsole():
    
    def __init__(self):
        self.Game_console = SudokuGame()

    def error_message(self, text):
        '''
        display an error
        '''
        print text
            
    def solve(self):
        '''
        Options to solve sudoku class need to start
        '''
           
        print "\n ======================================" 
        print "         Solve Sudoku "
        print "======================================" 
        print "\n1: Enter the Sudoku by file"
        print "2: Enter the Sudoku by consola"
        print "3: Back"
        option = self.enter_option(3,"\n Please enter an option: ")
        
        options_solve = {1: self.solve_from_a_file, 2: self.solve_from_console, 3: self.menu_ini}
        options_solve.get(option)()
    
    def menu_ini(self):
        return
    
    def solve_from_a_file(self):
        '''
        Solve a Sudoku with data from a file
        '''
        file_path = raw_input("\n Enter the path where the file is located: ")
        file_name = raw_input(" Enter the file name to read and solve the Sudoku: ")
        
        solved = self.Game_console.solve_sudoku_from_file(file_path, file_name)
        self.display_or_export_sudoku_solved(solved)
        input("Press any key to continue...")
        
    def solve_from_console(self):
        '''
        Solve a Sudoku with data entered from console
        '''
        print "===================================="    
        print "        Input instructions"
        print "===================================="
        print("1) Enter 81 numbers and press Enter key.")
        print("2) Use '0' or '.' to make reference to empty slots.")
        print("3) Press Enter key, to fill the rest with empty slots")
        print("4) only numbers are allowed")
        print("5) To exit this option press Q key\n")
        
        flag = False
        while not flag:
            input_text = raw_input("Start to enter numbers: ")
            if(input_text in "qQ"):
                flag = False
                break
            input_text, flag =self.Game_console.validate_text(input_text)
            
        if(flag):
            dictionary = input_text
            solved = self.Game_console.solve_sudoku_from_console(dictionary)
            self.display_or_export_sudoku_solved(solved)
            raw_input("Press any key to continue...")
    
    def display_or_export_sudoku_solved(self, dictionary):
        '''
        Print and/or export the solution
        '''
        alg =self.Game_console.xml_config_file.get_xml_value("default_algorithm")
        print 'testing..', alg
        output =self.Game_console.xml_config_file.get_xml_value("solver_output_type")
        output = output.lower()
            
        print "====================================================="    
        print "The algorithm used to solve is: ", alg.upper()
        print "====================================================="
      
        if (output == 'display by console'):
            self.Game_console.display(dictionary)
        if (output == 'export to file'):
            self.Game_console.display(dictionary)
            self.Game_console.txtfile.write_file(dictionary)
            print "\n...........The solution was exported to the file...........\n"
            os.system("cls")
                      
    
    def enter_option(self, length,text,error="Incorrect input!. \
                                        Please enter a proper option."):
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
    
        
    def exit_game(self):
        print "............Exist.............\n"