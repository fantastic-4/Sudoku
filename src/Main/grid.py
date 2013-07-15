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
        
    def validate_values(self,grid):
        '''Function to validate the values on grid given.
            Return True if their values are numeric or False if their not.'''
        full_line=""
        for line in grid:
            full_line += (line.strip(" ").strip("\n"))
        chars = [c for c in grid if c in self.digits or c in "0."]
        if len(chars) == 81 and len(full_line)==len(chars):
            return True
        else:
            return False
         
    def __get_ini_row_and_ini_col__(self,key):
        '''Function to set the top-left coordinate of the square where
            the number is about to fit
            Return 2 variables, row and column where the square begins'''
        row = key[0]
        col = key[1]
        if(row=="A" or row=="B" or row=="C"): ini_row = 0
        elif(row=="D" or row=="E" or row=="F"): ini_row = 3
        else: ini_row = 6     
        if(col=="1" or col=="2" or col=="3"): ini_col = 1
        elif(col=="4" or col=="5" or col=="6"): ini_col = 4
        else: ini_col = 7
        return ini_row,ini_col
    
    def check_square(self,num,key, values):
        '''Function to validate if the number is already in the square 3x3
            Return True if can be set on the square, False if the number is already on it'''
        flag = True
        ini_row, ini_col = self.__get_ini_row_and_ini_col__(key)
        lim_row = ini_row + 2
        aux = ini_col
        lim_col = ini_col + 2
        while ini_row <= lim_row and flag:
            ini_col = aux
            while ini_col <= lim_col:
                if(values[self.rows[ini_row]+str(ini_col)] == num
                    and key != self.rows[ini_row]+str(ini_col)
                    and values[self.rows[ini_row]+str(ini_col)] != "0"):
                    flag = False
                    break
                ini_col += 1
            ini_row += 1
        return flag

    def check_lines(self,num, key, values):
        '''Function to validate if the number is already in the row or column
            Return True if can be set on the cell,
            False if the number is already on row or column'''   

        flag = True
        row = key[0]
        col = key[1] 
        for i in self.digits:
            if(values[(row+i)] == num and not(i in key)
                and values[(row+i)] != "0"):
                flag = False
                break
        if(flag):
            for j in self.rows:
                if(values[j+col] == num and not(j in key)
                    and values[j+col] != "0"):
                    flag = False
                    break
        return flag

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
        