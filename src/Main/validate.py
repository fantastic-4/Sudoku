class Validate:
    '''this Class is used to validate if the string has only 0, dot or this has length  equal to 81 '''
    def __init__(self):
        self.digits   = "123456789"
    
    def validate_values(self,grid):
        #this only return True or False
        full_line=""
        for line in grid:
            full_line += (line.strip(" ").strip("\n"))
        chars = [c for c in grid if c in self.digits or c in "0."]
        if len(chars) == 81 and len(full_line)==len(chars):
            return True
        else:
            return False