class Grid:
    
    def __init__(self):
        self.dictionary_of_grid = None
        self.digits   = "123456789"
        self.rows     = "ABCDEFGHI"
        self.cols     = self.digits
        self.squares  = self.__set_matrix__(self.rows, self.cols)
        self.squares  = self.__set_matrix__(self.rows, self.cols)
        self.unitlist = ([self.__set_matrix__(self.rows, c) for c in self.cols] +
            [self.__set_matrix__(r, self.cols) for r in self.rows] +
            [self.__set_matrix__(rs, cs) for rs in ("ABC","DEF","GHI")
             for cs in ("123","456","789")])

        self.units = dict((s, [u for u in self.unitlist if s in u])
                     for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s],[]))-set([s]))
                     for s in self.squares)
    
    def __set_matrix__(self, A, B):
        '''__set_matrix__ product of elements in A and elements in B.'''
        return [a+b for a in A for b in B]

    def set_values(self,gridx):
        '''Function to create the grid using a grid list'''       
        chars = [c for c in gridx]
        return dict(zip(self.squares, chars))

    def validate_grid(self, grid_string):
        '''Function to validate the string given, if the values,
            size and order of values is correct,
            then it will be converted into a dictionary to be solved'''
        flag = self.validate_values(grid_string)
        if(flag):
            self.dictionary_of_grid = self.set_values(grid_string)
            for row in self.rows:
                for column in self.cols:
                    if(not self.check_lines(self.dictionary_of_grid[row+column],
                        row+column, self.dictionary_of_grid)
                        and not self.check_square(self.dictionary_of_grid[row+column],
                        row+column, self.dictionary_of_grid)):
                        flag = False                        
                        break
                if(not flag): break
        return flag
    
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
        