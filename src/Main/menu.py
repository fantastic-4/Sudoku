from Main.sudoku_game import SudokuGame

gamefromfile = SudokuGame()

def errorMessage():
    print "Incorrect input. Please enter a proper option."
    
def solve():   
    print "\n1: Enter the Sudoku by file"
    print "2: Enter the Sudoku by consola"
    print "3: Back"
    option = input(" Please select an option: ")
    
    options = {1: solve_from_a_file, 2: solve_from_console, 3: menu_ini}
    options.get(option)()

def solve_from_a_file():
    file_path = raw_input("\n Please enter the path where the file is located (Ex: C:\Sudoku) > ")
    file_name = raw_input(" Please enter the file name to read and solve the Sudoku (Ex: sudoku_easy.txt): ")
    
    solved = gamefromfile.solve_sudoku_from_file(file_path, file_name)
    alg = gamefromfile.xml_config_file.get_xml_value("default_algorithm").lower()
    output = gamefromfile.xml_config_file.get_xml_value("solver_output_type").lower()
        
    print "====================================================="    
    print "The algorithm used to solve is: ", alg.upper()
    print "====================================================="
  
    if (output == 'console'):
        print gamefromfile.grid.display(solved)
    if (output == 'file'):
        gamefromfile.txtfile.write_file(solved)
    print "\n.............The solution was exported to the file.............\n"

def solve_from_console():
    pass

     
def play_game():
    print "\n............This is not implemented yet..............\n"

def configure_settings():

    display_current_values()
    num = submenu_modify_values()
    tags = {1: "default_algorithm", 2: "solver_output_type", 3: "difficulty_level"}
    
    if (num == 4):
        menu_ini()
    else:
        option = display_options(num)
        if not (option == 'Back'):
            gamefromfile.set_xml_value(option,tags.get(num))
            print ".........Value updated....."
        configure_settings()
    
def display_current_values():
    print "\n ======================================" 
    print "         Current Values "
    print "======================================" 
    print "Algorithm: ", gamefromfile.get_xml_value("default_algorithm").upper()
    print "Output type: ", gamefromfile.get_xml_value("solver_output_type").upper()
    print "level: ", gamefromfile.get_xml_value("difficulty_level").upper()
    print "======================================"    
    
def submenu_modify_values():
    print "--------------------------------------"    
    print "Modify Values"
    print "--------------------------------------"    
          
    print "1: Change algorithm"
    print "2: Change output type"
    print "3: Change level"
    print "4: Back"
    return input("\n Please enter an option: \n")


def display_options(num):
    options1 = ["1: Norvig","2: Brute", "3: Back" ]
    options2 =  ["1: Console", "2: Export to file", "3: Back"]
    options3 =  ["1: Easy", "2: Medium", "3: Hard", "4: Back"]
    
    toSelect = {1:options1, 2: options2, 3:options3 }
    for option in toSelect.get(num):
        print option
    
    option = input("\n Please select an option: ")
    return toSelect.get(num)[option-1][3:]
    
    
def exit_game():
    print "............Exist.............\n"

options = {1: solve, 2: play_game, 3: configure_settings, 4: exit_game}



def menu_ini():
    while (True):
        print "======================================"    
        print "Administration Console for Sudoku Game"
        print "======================================"
        
        print "1: Solve a Sudoku"
        print "2: Play Sudoku"
        print "3: Configure Settings"
        print "4: Exit"
        
        num = input("\n Please enter an option: ")
        options.get(num, errorMessage)()
        if (num == 4): break
       
menu_ini()