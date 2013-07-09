from Main.validate import Validate
class Grid:
    
    def __init__(self):
        self.validate=Validate()
        self.digits   = '123456789'
        self.rows     = 'ABCDEFGHI'
        self.cols     = self.digits
        self.squares  = self.__set_matrix__(self.rows, self.cols)
        self.unitlist = ([self.__set_matrix__(self.rows, c) for c in self.cols] +
            [self.__set_matrix__(r, self.cols) for r in self.rows] +
            [self.__set_matrix__(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

        self.units = dict((s, [u for u in self.unitlist if s in u])
                     for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s],[]))-set([s]))
                     for s in self.squares)

## Throughout this program we have:
##   r is a row,    e.g. 'A'
##   c is a column, e.g. '3'
##   s is a square, e.g. 'A3'
##   d is a digit,  e.g. '9'
##   u is a unit,   e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
##   grid is a grid,e.g. 81 non-blank chars, e.g. starting with '.18...7...
##   values is a dict of possible values, e.g. {'A1':'12349', 'A2':'8', ...}  
      
    def __set_matrix__(self, A, B):
        "__set_matrix__ product of elements in A and elements in B."
        return [a+b for a in A for b in B]
    
    
    def set_values(self,gridx):#this only create the grid using a grid list
        if self.validate.validate_values(gridx):
            chars = [c for c in gridx]
            return dict(zip(self.squares, chars))
        else: 
            print "The content is not valid"
            return None
        
    def display(self,values):
        width = 1+max(len(values[s]) for s in self.squares)
        line = '+'.join(['-'*(width*3)]*3)
        solved_row = ''
        for r in self.rows:
            "Before print on console, add the rows to the output var" 
            solved_row += ''.join(values[r+c].center(width)+('|' if c in '36' else '')for c in self.cols) 
            solved_row += '\n'
            if r in 'CF':
                "Add to output var"
                solved_row += (line+'\n')
        return solved_row
        
