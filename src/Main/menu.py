import os
from Main.sudoku_game import SudokuGame

game = SudokuGame()

def errorMessage(text):
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
    
    options = {1: solve_from_a_file, 2: solve_from_console, 3: menu_ini}
    options.get(option)()

def solve_from_a_file():
    file_path = raw_input("\n Please enter the path where the file is located (Ex: C:\Sudoku) > ")
    file_name = raw_input(" Please enter the file name to read and solve the Sudoku (Ex: sudoku_easy.txt): ")
    
    solved = game.solve_sudoku_from_file(file_path, file_name)
    display_or_export_sudoku_solved(solved)
    
def solve_from_console():
    print "====================================================="    
    print "Input Sudoku game instructions"
    print "====================================================="
    print("1) Enter 81 numbers and press Enter key.")
    print("2) Use '0' or '.' to make reference to empty slots.")
    print("3) Press Enter key, before complete the 81 numbers, to fill the rest with empty slots.")
    print("4) Only Numbers are allowed, at any error you will be prompted to start again")
    print("5) To exit this option press Q key\n")
    
    flag = False
    while not flag:
        input_text = raw_input("Start to enter numbers: ")
        if(input_text in "qQ"):
            flag=False
            #solve()
            break
        input_text,flag = game.validate_text(input_text)
        
    if(flag):
        dictionary = input_text
    
        solved = game.solve_sudoku_from_console(dictionary)
        display_or_export_sudoku_solved(solved)

def display_or_export_sudoku_solved(dictionary):
    alg = game.xml_config_file.get_xml_value("default_algorithm").lower()
    output = game.xml_config_file.get_xml_value("solver_output_type").lower()
        
    print "====================================================="    
    print "The algorithm used to solve is: ", alg.upper()
    print "====================================================="
  
    if (output == 'display by console'):
        game.display(dictionary)
    if (output == 'export to file'):
        game.txtfile.write_file(dictionary)
        print "\n.............The solution was exported to the file.............\n"
        os.system("cls")

     
def play_game():
    print "\n............This is not implemented yet..............\n"

def configure_settings():

    display_current_values()
    num = submenu_modify_values()
    tags = {1: "default_algorithm", 2: "solver_output_type", 3: "difficulty_level", 4:"save_game_number"}
    
    if (num == 5):
        menu_ini()
    else:
        option = display_options(num)
        if not (option == 'Back'):
            game.set_xml_value(option,tags.get(num))
            print ".........Value updated....."
            os.system("cls")
        configure_settings()
    
def display_current_values():
    print "\n ======================================" 
    print "         Current Values "
    print "======================================" 
    print "Algorithm: ", game.get_xml_value("default_algorithm").upper()
    print "Output type: ", game.get_xml_value("solver_output_type").upper()
    print "level: ", game.get_xml_value("difficulty_level").upper()
    print "Number of saved games: ", game.get_xml_value("save_game_number")
    print "======================================"    
    
def submenu_modify_values():
   # print "--------------------------------------"    
    print "Modify Values"
    print "======================================"    
          
    print "1: Change algorithm"
    print "2: Change output type"
    print "3: Change level"
    print "4: Change number of saved games"
    print "5: Back"
    return enter_option(5,"\n Please enter an option: \n")
    


def display_options(num):
    algoritms = ["1: Norvig","2: Brute", "3: Back" ]
    outputTypes =  ["1: Display by console", "2: Export to file", "3: Back"]
    levels =  ["1: Easy", "2: Medium", "3: Hard", "4: Back"]   
    toSelect = {1:algoritms, 2: outputTypes, 3:levels}
    if num==4:
        value=enter_option(100, "\n Please enter new value: \n", "Incorrect input!. Please enter correct value")
        option=value
        return int(value)
    else:
        for option in toSelect.get(num):
            print option
        option = enter_option(4,"\n Please enter an option: \n")
        return toSelect.get(num)[int(option)-1][3:]
        

def enter_option(len,text,error="Incorrect input!. Please enter a proper option."):
    while True:
        num= raw_input(text)
        try:
            num=float(num)
            if (num <= len):
                return num
                break
            else:
                errorMessage(error)
                pass
        except ValueError:
            errorMessage(error)
            pass

    
def exit_game():
    print "............Exist.............\n"
    os.system("cls")

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
        
        
        num = enter_option(4, "\n Please enter an option: \n")
        
        options.get(num, errorMessage)()
        if (num == 4): 
            os.system('cls')
            break
        
       
menu_ini()