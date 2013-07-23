'''This class is a subclass of File class'''
from File.file import File
from Parser.validator import Validator

class Csvfile(File):
    
    def __init__(self,path, name):
        ''' Start some variables that we need to CSV file
        this is subclass from File'''
        
        File.__init__(self,path,name)
        self.delimiter = ","
        self.validator = Validator()
        

    def read_file(self):
        '''Function to read a CSV file.'''
        full_line = ""
        file_to_read = self.open_file()
        if(file_to_read != None):
            lines = file_to_read.readlines()
            self.close_file(file_to_read)
            for line in lines:
                if (line != '\n'):              
                    full_line += (self.__line_splitter(line.strip("\n")))
        if(self.validator.validate_values(full_line)): 
            return full_line

    
      
    def __line_splitter(self,line):
        '''Function to split a string of characters according\
         to the 3 principal delimiters on a CSV file.
       Return the line split by common delimiters on CSV files.'''  
        
        new_line = ""
        if("," in line):
            line_splitted = (line.split(","))
            self.delimiter = ","
        elif(";" in line):
            line_splitted = (line.split(";"))
            self.delimiter = ";"
        elif("\t" in line):
            line_splitted = (line.split("\t"))
            self.delimiter = "\t"
        
        for character in line_splitted: 
            new_line += character
        return new_line
    
    
    def write_file(self, dictionary):
        '''Function to export result in a csv file by preparing\
         the result in the same format as it was read'''
        
        text_to_be_written = ""
        rows = "ABCDEFGHI"
        columns = "123456789"
        chars_counter = 0
        for row in rows:
            for column in columns:
                if(chars_counter == 9):
                    text_to_be_written += self.delimiter
                    chars_counter = 0
                text_to_be_written += dictionary[row + column]
                chars_counter += 1
                
        self.create_file(text_to_be_written)
            