class File:
    
    def __init__(self, path, name):
        
        self.path = path
        self.file_name = name

        
    '''Function to open a CSV file.
       Return file opened.'''
    def open_file(self):
        file_to_open = None
        self.clean_path()
        try:
            file_to_open = open(self.path + "\\" + self.file_name,"r")
        except IOError:
            print("File: ",self.file_name," was not found on path: ",self.path)
        return file_to_open
        
    '''Function to close CSV file'''
    def close_file(self, file_opened):
        file_opened.close()
        
    '''Function to create a file.'''
    def create_file(self,text_to_be_written):
        file_to_write = open(self.path + "\\" + self.file_name,"w")
        file_to_write.write(text_to_be_written)
        self.close_file(file_to_write)
        
    def clean_path(self):
        if(self.path[len(self.path)-1] == "\\"):
            self.path = self.path[0:len(self.path)-1]
            self.clean_path()    