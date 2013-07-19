'''
Sudoku
'''
import os, sys
sys.path.append("../../src")
from Main.sudoku_game import SudokuGame

Game_first = SudokuGame()

def error_message(text):
    '''
    display an error
    '''
    print text
        
def solve():
    '''
    Options to solve sudoku class need to start
    '''
       
    print "\n ======================================" 
    print "         Solve Sudoku "
    print "======================================" 
    print "\n1: Enter the Sudoku by file"
    print "2: Enter the Sudoku by consola"
    print "3: Back"
    option = enter_option(3,"\n Please enter an option: \n")
#    os.system("cls")
    
    options_solve = {1: solve_from_a_file, 2: solve_from_console, 3: menu_ini}
    options_solve.get(option)()

def solve_from_a_file():
    '''
    Solve a Sudoku with data from a file
    '''
    file_path = raw_input("\n Enter the path where the file is located: ")
    file_name = raw_input(" Enter the file name to read and solve the Sudoku: ")
    
    solved = Game_first.solve_sudoku_from_file(file_path, file_name)
    display_or_export_sudoku_solved(solved)
    os.system("cls")
    
def solve_from_console():
    '''
    Solve a Sudoku with data entered from console
    '''
    print "====================================================="    
    print "Input Sudoku Game_first instructions"
    print "====================================================="
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
        input_text, flag = Game_first.validate_text(input_text)
        
    if(flag):
        dictionary = input_text
    
        solved = Game_first.solve_sudoku_from_console(dictionary)
        display_or_export_sudoku_solved(solved)

def display_or_export_sudoku_solved(dictionary):
    '''
    Print and/or export the solution
    '''
    alg = Game_first.xml_config_file.get_xml_value("default_algorithm")
    alg.lower()
    output = Game_first.xml_config_file.get_xml_value("solver_output_type")
    output.lower()
        
    print "====================================================="    
    print "The algorithm used to solve is: ", alg.upper()
    print "====================================================="
  
    if (output == 'display by console'):
        Game_first.display(dictionary)
    if (output == 'export to file'):
        Game_first.txtfile.write_file(dictionary)
        print "\n...........The solution was exported to the file...........\n"
        os.system("cls")

     
def play_game():
    '''
    To player
    '''
    print "\n............This is not implemented yet..............\n"

def configure_settings():
    '''
    To modify configuration values
    '''
    display_current_values()
    num = submenu_modify_values()
    tags = {1: "default_algorithm", 2: "solver_output_type",\
             3: "difficulty_level", 4:"save_game_number"}
    
    if (num == 5):
        menu_ini()
    else:
        option = display_options(num)
        if not (option == 'Back'):
            Game_first.set_xml_value(option,tags.get(num))
            print ".........Value updated....."
            os.system("cls")
        configure_settings()
    
def display_current_values():
    print "\n ======================================" 
    print "         Current Values "
    print "======================================" 
    print "Algorithm: ", Game_first.get_xml_value("default_algorithm").upper()
    print "Output type: ",\
                        Game_first.get_xml_value("solver_output_type").upper()
    print "level: ", Game_first.get_xml_value("difficulty_level").upper()
    print "Number of saved games: ",\
                        Game_first.get_xml_value("save_game_number")
    print "======================================"    
    
def submenu_modify_values():
    print "--------------------------------------"    
    print "Modify Values"
    print "======================================"    
          
    print "1: Change algorithm"
    print "2: Change output type"
    print "3: Change level"
    print "4: Change number of saved games"
    print "5: Back"
    return enter_option(5,"\n Please enter an option: \n")
    


def display_options(num):
    algoritms = ["1: Norvig", "2: Brute", "3: Back" ]
    outputTypes =  ["1: Display by console", "2: Export to file", "3: Back"]
    levels =  ["1: Easy", "2: Medium", "3: Hard", "4: Back"]   
    select = {1:algoritms, 2: outputTypes, 3:levels}
    if num == 4:
        value=enter_option(100, "\n Please enter new value: \n",
                            "Incorrect input!. Please enter correct value")
        option=value
        return int(value)
    else:
        for option in select.get(num):
            print option
        option = enter_option(4,"\n Please enter an option: \n")
        return select.get(num)[int(option)-1][3:]
        

def enter_option(length,text,error="Incorrect input!. \
                                    Please enter a proper option."):
    while True:
        num = raw_input(text)
        try:
            num = int(num)
            if (num <= length):
                return num
                break
            else:
                error_message(error)
                pass
        except ValueError:
            error_message(error)
            pass

    
def exit_game():
    print "............Exist.............\n"


options = {1: solve, 2: play_game, 3: configure_settings}
def menu_ini():
    os.system("cls")
    while (True):
        print "======================================"    
        print "Administration Console for Sudoku Game_first"
        print "======================================"
        
        print "1: Solve a Sudoku"
        print "2: Play Sudoku"
        print "3: Configure Settings"
        print "4: Exit"
        
        
        num = enter_option(4, "\n Please enter an option: \n")
        
        
        if (num == 4): 
            print "............Exist.............\n"
            break
        else:
            
            options.get(num, error_message)()
            break
        
menu_ini()