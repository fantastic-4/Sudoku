from Main.validator import Validator
class Grid:
    
    def __init__(self):
        
        self.values = None
        self.validator = Validator()

        self.cols     = self.validator.digits
        self.squares  = self.__set_matrix__(self.validator.rows, self.cols)
        self.unitlist = ([self.__set_matrix__(self.validator.rows, c) for c in self.cols] +
            [self.__set_matrix__(r, self.cols) for r in self.validator.rows] +
            [self.__set_matrix__(rs, cs) for rs in ("ABC","DEF","GHI")
             for cs in ("123","456","789")])

        self.units = dict((s, [u for u in self.unitlist if s in u])
                     for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s],[]))-set([s]))
                     for s in self.squares)

    '''Throughout this program we have:
      r is a row,    e.g. "A"
      c is a column, e.g. "3"
      s is a square, e.g. "A3"
      d is a digit,  e.g. "9"
      u is a unit,   e.g. ["A1","B1","C1","D1","E1","F1","G1","H1","I1"]
      grid is a grid,e.g. 81 non-blank chars, e.g. starting with ".18...7...
      values is a dict of possible values, e.g. {"A1":"12349", "A2":"8", ...}'''  
    
    def __set_matrix__(self, A, B):
        '''__set_matrix__ product of elements in A and elements in B.'''
        
        return [a+b for a in A for b in B]
    
    def set_values(self,gridx):
        '''Function to create the grid using a grid list'''
        
        chars = [c for c in gridx]
        self.values = dict(zip(self.squares, chars))
        
    def display(self,values):
        width = 1+max(len(values[s]) for s in self.squares)
        line = "+".join(["-"*(width*3)]*3)
        solved_row = ""
        for r in self.validator.rows:
            '''Before print on console, add the rows to the output var''' 
            solved_row += "".join(values[r+c].center(width)
                                  +("|" if c in "36" else "")for c in self.validator.digits) 
            solved_row += "\n"
            if r in "CF":
                '''Add to output var'''
                solved_row += (line+"\n")
        return solved_row
    
    
    
    def validate_grid(self, grid_string):
        '''Function to validate the string given, if the values,
           size and order of values is correct,
           then it will be converted into a dictionary to be solved'''
        flag = self.validator.validate_values(grid_string)
        if(flag):
            self.set_values(grid_string)
            for row in self.validator.rows:
                for column in self.validator.digits:
                    if(not self.validator.check_lines(self.values[row+column],
                                            row+column, self.values)
                       and not self.validator.check_square(self.values[row+column],
                                                 row+column, self.values)):
                        flag = False                        
                        break
                if(not flag): break
        return flag