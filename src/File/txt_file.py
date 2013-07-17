import datetime
from File.file import File
from Main.display import Display

class TXT_File(File):
    
    def __init__(self,path , name):
        File.__init__(self, path, name)
        self.file=File(path,name)
        self.display=Display()


    def read_file(self, sep='\n'):
        '''Function to read a file from txt file until found separator= ======
        , and return the sudoku game as string'''
        value=""
        fileO= self.open_file()
        file_string = fileO.read().strip().split(sep)
        for i in file_string:
            if i!="========":
                value += i
            else:
                return value

    def write_file(self, values):
        '''This method save the game into TXT called Solved_game_timeStamp.txt
         file where the path will be defined in main class'''
        self.file_name=self.timeStamped("Solved_game")
        value_r="======================== \n"\
        +"    Sudoku Solved:    \n"\
        +"======================== \n"
        value_r+=self.display.display(values)
        self.create_file(value_r)

    def timeStamped(self,fname, fmt="{fname}_%Y_%m_%d_%H_%M_%S.txt"):
        '''Method to add the timestamp to a saved file '''
        return datetime.datetime.now().strftime(fmt).format(fname=fname)
    
    def save_game(self, value, tim):
        '''this method receives the dict and the time in mins:seconds and save 
        it into saved_game_timestamp.txt file'''
        self.file_name=self.timeStamped("Saved_game")
        new_string = ""
        rows = "ABCDEFGHI"
        columns = "123456789"
        for row in rows:
            for column in columns:
                new_string += value[row + column]

        new_string+=","+tim
        self.create_file(new_string)
            
            





