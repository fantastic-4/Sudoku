'''
Submenu to solve a Sudoku game
'''
import os

class SolveConsole():
    '''
    Solve a sudoku game from console
    '''
    def __init__(self, sudoku):
        self.game_console = sudoku
           
    def solve(self):
        '''
        Options to solve sudoku class need to start
        '''
        os.system("cls")   
        print "\n======================================" 
        print "         Solve Sudoku "
        print "======================================" 
        print "\n1: Enter the Sudoku by file"
        print "2: Enter the Sudoku by console"
        print "3: Back"
        option = self.enter_option(3,"\nPlease enter an option: ")
        
        options_solve = {1: self.solve_from_a_file, 2: self.solve_from_console, \
                          3: self.menu_ini}
        options_solve.get(option)()
    
    def menu_ini(self):
        '''
        Back to the principal menu 
        '''
        return
    
    def solve_from_a_file(self):
        '''
        Solve a Sudoku with data from a file
        '''
         
        while True:
            valuepath = raw_input("\nEnter the path where the file is located: ")
            head = os.path.split(valuepath)
            newhead = head[0]+ head[1]
            if head[1] == "" :
                newhead = head[0]
            elif(head[1][-4:-3] == "."):
                newhead = head[0]
            if self.verify_path(newhead):
                file_path = newhead
                break
            else: 
                print "The path does not exist, try again.."
                
        while True:
            valuename = raw_input("\nEnter the file name to\
 read and solve the Sudoku: ")
            if self.verify_file(file_path+"\\"+valuename):
                file_name = valuename
                break
            else:
                print "The file does not exist, try again.."            
        
        
        solved = self.game_console.solve_sudoku_from_file(file_path, file_name)
    #    original1=self.game_console.get_original_string(file_path, file_name)

        self.display_or_export_sudoku_solved(solved)
        raw_input("Press any key to continue...")
        
    def verify_path(self, ispath):
        '''
        Verify if the path typed exists
        '''
        if os.path.exists(ispath):
            return True
        else: 
            return False
        
    def verify_file(self, isfile):
        '''
        Verify if the file typed exists
        '''
        if os.path.isfile(isfile):
            return True
        else: 
            return False
        
    def solve_from_console(self):
        '''
        Solve a Sudoku with data entered from console
        '''
        print "===================================="    
        print "        Input instructions"
        print "===================================="
        print("- Enter 81 numbers and press Enter key.")
        print("- Use '0' or '.' to make reference to empty slots.")
        print("- Press Enter key, to fill the rest with empty slots")
        print("- Only numbers are allowed")
        print("- To exit, press 'Q' or just 'Enter' key.")
        
        flag = False
        while not flag:
            input_text = raw_input("Start to enter numbers: ")
            if(input_text in "qQ"):
                flag = False
                break
            input_text, flag = self.game_console.validate_text(input_text)
            
        if(flag):
            dictionary = input_text
            solved = self.game_console.solve_sudoku_from_console(dictionary)
            self.display_or_export_sudoku_solved(solved)
            raw_input("Press any key to continue...")
    
    def display_or_export_sudoku_solved(self, dictionary):
        '''
        Print and/or export the solution
        '''
        alg = self.game_console.xml_config_file.\
        get_xml_value("default_algorithm")
        output = self.game_console.xml_config_file.\
        get_xml_value("solver_output_type")
        output = output.lower()
        
        print "==========================\t\t" + \
        "=========================="  
        print "      Original Game: \t\t\t" + \
        " solved using: ", alg.upper()
        print "==========================\t\t" + \
        "=========================="
        sudoku_solved = self.game_console.display_dic.\
        display_sudoku_before_and_after_solved_it(self.game_console.original, dictionary)
      
        if (output == 'display by console'):
            self.game_console.display_string(sudoku_solved)
        if (output == 'export to file'):
            self.game_console.display_string(sudoku_solved)
            self.game_console.file_read.write_file(sudoku_solved)
            print "\n...The solution was exported successfully to the path: %s\
             \n" %self.game_console.file_read.path
            os.system("cls")
                      
    
    def enter_option(self, length, text, error = "Incorrect input!.\
        \nPlease enter a proper option."):
        '''
        Verify if the option is correct
        '''
        while True:
            num = raw_input(text)
            try:
                num = int(num)
                if (num <= length):
                    return num
                    break
                else:
                    self.error_message(error)
            except ValueError:
                self.error_message(error)
    
    def error_message(self, text):
        '''
        display an error
        '''
        print text
