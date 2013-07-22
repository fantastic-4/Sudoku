'''This class create a file, read file and write a file'''
class File:
    
    def __init__(self, path, name):
        '''
        Initialize the path and name
        '''
        self.path = path
        self.file_name = name

        
    def open_file(self):
        '''Open a file and returns file opened.'''
        file_to_open = None
        self.clean_path()
        try:
            file_to_open = open(self.path + "\\" + self.file_name,"r")
        except IOError:
            print("File: ",self.file_name," was not found on path: ",self.path)
        return file_to_open
        
    
    def close_file(self, file_opened):
        '''Function to close file'''
        file_opened.close()
        

    def create_file(self,text_to_be_written):
        '''Function to create a file.'''
        file_to_write = open(self.path + "\\" + self.file_name,"w")
        file_to_write.write(text_to_be_written)
        self.close_file(file_to_write)
        
    def clean_path(self):
        '''Clean the path if this has more than on \\'''
        if(self.path[len(self.path)-1] == "\\"):
            self.path = self.path[0:len(self.path)-1]
            self.clean_path()    