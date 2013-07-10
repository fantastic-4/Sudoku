class Validate:
    '''this Class is used to validate if the string has only 0, dot or this has length  equal to 81 '''
    def __init__(self):
        self.digits   = "123456789"
    
    def validate_values(self,grid):#this only return True or False

        chars = [c for c in grid if c in self.digits or c in '0.']
        if len(chars) == 81:
            return True
        else:
            return False
        
        