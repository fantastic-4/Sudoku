from Parser.validator import Validator
class Grid:
    
    def __init__(self):
        self.validator = Validator()
        
        self.dictionary_of_grid = None
        self.digits   = "123456789"
        self.rows     = "ABCDEFGHI"
        self.cols     = self.digits
        self.squares  = self.__set_matrix(self.rows, self.cols)
        self.unitlist = ([self.__set_matrix(self.rows, c) for c in self.cols] +
            [self.__set_matrix(r, self.cols) for r in self.rows] +
            [self.__set_matrix(rs, cs) for rs in ("ABC","DEF","GHI")
             for cs in ("123","456","789")])

        self.units = dict((s, [u for u in self.unitlist if s in u])
                     for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s],[]))-set([s]))
                     for s in self.squares)
    
    def __set_matrix(self, A, B):
        '''set_matrix product of elements in A and elements in B.'''
        return [a+b for a in A for b in B]

    def set_values(self,gridx):
        '''Function to create the grid using a grid list'''       
        chars = [c for c in gridx]
        return dict(zip(self.squares, chars))

    def validate_grid(self, grid_string):
        '''Function to validate the string given'''
        flag = self.validator.validate_values(grid_string)
        if(flag):
            self.dictionary_of_grid = self.set_values(grid_string)
            for row in self.rows:
                for column in self.cols:
                    if(not self.validator.check_lines(self.dictionary_of_grid[row+column],
                                                      row+column,
                                                      self.dictionary_of_grid)
                        or not self.validator.check_square(self.dictionary_of_grid[row+column],
                                                            row+column,
                                                            self.dictionary_of_grid)):
                        flag = False                        
                        break
                if(not flag): break
        return flag
    
        