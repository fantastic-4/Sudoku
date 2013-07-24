'''
Submenu to configure settings of Sudoku game 
'''
import os


class ConfigureConsole:
    '''
    This class handle all configuration stuff
    '''
    def __init__(self, sudoku):
        self.settings = sudoku
        
    def configure_settings(self):
        ''' This function is the main, this will be called from menu'''
        
        self.display_current_values()
        num = self.submenu_modify_values()
        tags = {1: "default_algorithm", 2: "solver_output_type", \
                 3: "difficulty_level", 4: "save_game_number"}
        
        if (num == 5):
            return
        else:
            option = self.display_options(num)
            if not (option == 'Back'):
                self.settings.set_xml_value(option, tags.get(num))
                print "............Value updated............"
                os.system("cls")
            self.configure_settings()

    def display_options(self, num):
        ''' Displays all option for configuration that will be changed'''
        algoritms = ["1: Norvig", "2: Brute", "3: Dlx", "4: Back" ]
        output_types =  ["1: Display by console", "2: Export to file", "3: Back"]
        levels =  ["1: Easy", "2: Medium", "3: Hard", "4: Back"]   
        to_select = {1: algoritms, 2: output_types, 3: levels}
        if num == 4:
            value = self.enter_option(100, "\n Please enter new value: ", \
                   "\nIncorrect input!. Please enter correct value")
            option = value
            return int(value)
        else:
            for option in to_select.get(num):  
                print option
            if num == 2:
                option = self.enter_option(3, "\n Please enter an option****:\n")
            else:
                option = self.enter_option(4, "\n Please enter an option...:\n")
            return to_select.get(num)[int(option)-1][3:]

    def display_current_values(self):
        ''' Displays current values in config file xml'''
        
        print "\n======================================" 
        print "         Current Values "
        print "======================================" 
        print "Algorithm: ", self.settings.get_xml_value("default_algorithm").\
        upper()
        print "Output type: ", \
         self.settings.get_xml_value("solver_output_type").upper()
        print "level: ", \
        self.settings.get_xml_value("difficulty_level").upper()
        print "Number of saved games: ", \
         self.settings.get_xml_value("save_game_number")
        print "======================================"    
        
    def submenu_modify_values(self):  
        '''Displays all options that has the config file xml\
         that we can change'''
         
        print "\tModify Values"
        print "======================================"    
              
        print "1: Change algorithm"
        print "2: Change output type"
        print "3: Change level"
        print "4: Change number of saved games"
        print "5: Back"
        return self.enter_option(5,"\n Please enter an option: \n")

    def enter_option(self, length, text, \
                     error="Incorrect input!. Please enter a proper option."):
        ''' asks for an value from input and validate 
        if this option is correct, this use error_message function'''
        
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
        To display an error message
        '''
        print text
