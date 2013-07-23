class Validator:
    
    def __init__(self):
        self.digits   = "123456789"
        self.rows     = "ABCDEFGHI"
    
    def validate_values(self,grid):
        '''Function to validate the values on grid given.
       Return True if their values are numeric or False if their not.'''
    
        full_line=""
        for line in grid:
            full_line += (line.strip(" ").strip("\n"))
        chars = [c for c in grid if c in self.digits or c in "0."]
        return (len(chars) == 81 and len(full_line) == len(chars))
        
    def set_matrix(self, A, B):
        '''__set_matrix__ product of elements in A and elements in B.'''
        
        return [a+b for a in A for b in B]
        
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