# from File.txt_file import TXT_File
# from Main.grid import Grid
# from Solver.norvig import Norvig
# from Solver.brute import Brute
# from File.config_file_xml import Xml_file
from Main.sudoku_game import SudokuGame 


# xml_config_file = Xml_file('../File/', 'xml_config_file')    
def errorMessage():
    print "Incorrect input. Please enter a proper option."
    
def solve():
#     norvig=Norvig()
#     grid=Grid()
#     brute=Brute()
    
    file_path = raw_input("\n Please enter the path where the file is located (Ex: C:\Sudoku) > ")
    file_name = raw_input(" Please enter the file name to read and solve the Sudoku (Ex. sudoku_easy.txt): ")
    
    gamefromfile = SudokuGame()
    gamefromfile.solve_sudoku(file_path, file_name)
    
#     txtfile=TXT_File(file_path, file_name)
#     iofile_easy=txtfile.read_file()
#     
#     algorithm = xml_config_file.get_xml_value("default_algorithm").lower()
#     output = xml_config_file.get_xml_value("solver_output_type").lower()
#     print algorithm
#     
#     dict_algorithm = {'norvig': norvig.solve(iofile_easy), 'brute': brute.solve(iofile_easy)}
#     sudoku_resolved=dict_algorithm.get(algorithm, errorMessage)
#     #print sudoku_resolved
#         
#     print "====================================================="    
#     print "The algorithm used to solve is: ", algorithm.upper()
#     print "====================================================="
#     #print grid.display(sudoku_resolved)
#     
#     
#     if (output == 'console'):
#         print grid.display(sudoku_resolved)
#     if (output == 'file'):
#         txtfile.file_name = 'Sudoku_resolved.txt'
#         txtfile.output_file(sudoku_resolved)
#         print "\n.............The solution was exported to the file.............\n"

def read_default_settings():
    pass
     
def play_game():
    print "\n............This is not implemented yet..............\n"

def configure_settings():

    print "\n ======================================" 
    print "         Current Values "
    print "======================================" 
    print "Algorithm: ", xml_config_file.get_xml_value("default_algorithm").upper()
    print "Output type: ", xml_config_file.get_xml_value("solver_output_type").upper()
    print "level: ", xml_config_file.get_xml_value("difficulty_level").upper()
    print "======================================"    
    
    print "======================================"    
    print "Modify Values\n"
    
      
    print "1: Change algorithm"
    print "2: Change output type"
    print "3: Change level"
    print "4: Back"
    num = input("\n Please enter an option: ")
    
    
    if (num == 1):
        ("Please select an option: ")
        print "1: Norvig"
        print "2: Brute"
        alg = ['Norvig', 'Brute']
        num = input("\n Please enter an option: ")
        xml_config_file.set_xml_value(alg[num-1],"default_algorithm")
        configure_settings()
    if (num == 2):
        ("Please select an option: ")
        print "1: Console"
        print "2: Export to file"
        outp = ['Console', 'File']
        num = input("\n Please enter an option: ")
        xml_config_file.set_xml_value(outp[num-1],"solver_output_type")
        configure_settings()
    if (num == 3):
        ("Please select an option: ")
        print "1: Easy"
        print "2: Medium"
        print "3: Hard"
        alg = ['Easy', 'Medium', 'Hard']
        num = input("\n Please enter an option: ")
        xml_config_file.set_xml_value(alg[num-1],"difficulty_level")
        configure_settings()
    
    if (num == 4): menu_ini()
    
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