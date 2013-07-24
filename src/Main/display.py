'''
Sudoku Game
'''
class Display:
    '''
    Class Display to format the dictionary
    '''
    def __init__(self):
        self.rows     = "ABCDEFGHI"
        self.cols     = "123456789"
        self.squares  = [a+b for a in self.rows for b in self.cols]
        
    def display(self, values):
        '''This method return the sudoku board in order to print in console or 
        save in file'''     
        solved_row = "    1 2 3  4 5 6  7 8 9 \n    --------------------\n"
        dict_rows = {"A":"A:  ", "B":"B:  ", "C":"C:  ", "D":"D:  ", "E":"E:  ",
                     "F":"F:  ", "G":"G:  " , "H":"H:  ", "I":"I:  ",}          
        width = 1+max(len(values[s]) for s in self.squares)
        line = "    "+ "+".join(["-"*(width*3)]*3)
        for row in self.rows:
            solved_row += dict_rows[row]      
            solved_row += "".join(values[row+c].center(width)+\
                                  ("|" if c in "36" else "")for c in self.cols) 
            solved_row += "\n"
            if row in "CF":
                solved_row += (line+"\n")
        
        return solved_row
