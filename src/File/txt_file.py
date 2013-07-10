from File.file import File
from Main.grid import Grid

class TXT_File(File):
    
    def __init__(self,path , name):
        File.__init__(self, path, name)
        self.file=File(path,name)
        self.path=path
        self.name=name
        self.grid=Grid()

    '''Function to read a file from txt file until found separator= ======'''
    def read_file(self, sep='\n'):
        value=''
        fileO= self.open_file()
        file_string = fileO.read().strip().split(sep)
        for i in file_string:
            if i!="========":
                value += i
            else:
                if self.validate.validate_values(value):
                    return value
                else: 
                    print "the file is incorrect or more than 81"; 


                
    ''' this method is private and this only add enter to the string in order to get a list of 9 x 9 to print.'''
    def __add_enter_in_line__(self, string):
        text_to_be_written = ""
        rows = "ABCDEFGHI"
        columns = "123456789"
        chars = 0
        for row in rows:
            for column in columns:
                if chars == 9:
                    text_to_be_written +="\n"
                    chars=0 
                text_to_be_written += string[row + column]
                chars+=1
        return text_to_be_written

    '''this method save the file in named file inserted'''
    def output_file(self, values):
        #self.file_name="Solved_sudoku.txt"
        value_return=""
        value_return+=self.__add_enter_in_line__(values)+"\n\n"+self.grid.display(values)
        self.create_file(value_return)


