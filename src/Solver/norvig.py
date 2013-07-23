from Solver.solve_algorithm import SolveAlgorithm 
import time
from Parser.grid import Grid
class Norvig (SolveAlgorithm):
    '''
    This class is using some attributes from grid like:squares,
     cols, rows and this needs a value (not a grid) to print
    '''

    def __init__(self):
        SolveAlgorithm.__init__(self)
        self.grid = Grid() 

    def grid_to_dict(self,grid):
        '''Convert grid to a dict of possible values, {square: digits}, or
        return False if a contradiction is detected.'''
        values = dict((s,self.grid.digits) for s in self.grid.squares)
        for s,d in grid.items():
            if d in self.grid.digits and not \
            self.__eliminate_other_value(values, s, d):
                return False
        return values

    def __eliminate_other_value(self, values, s, d):
        '''Eliminate all other values (except d) from values[s] and propagate.
        Return values, except return False if a contradiction is detected.'''
        other_values = values[s].replace(d, '')
        if all(self.__eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False
        
    def __eliminate(self,values, s, d):
        '''eliminate d from values[s]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected.'''
        if d not in values[s]:
            return values
        values[s] = values[s].replace(d,'')
        if len(values[s]) == 0:
            return False
        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(self.__eliminate(values, s2, d2)\
                        for s2 in self.grid.peers[s]):
                return False
        for u in self.grid.units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                if not self.__eliminate_other_value(values, dplaces[0], d):
                    return False
        return values
    
    def solve(self,gridA): 
        '''verify if the grid is correct then call to search and transform 
        the grid to dict'''
        self.time_elapsed = time.clock()
        result = self.__search(self.grid_to_dict(gridA))
        self.time_elapsed = time.clock() - self.time_elapsed
        return result
 
    def __search(self,values):
        '''Using depth-first to search and propagate, try all possible 
        values.'''
        if values is False:
            return False
        if all(len(values[s]) == 1 for s in self.grid.squares):
            return values 
        n,s = min((len(values[s]), s) for s 
                  in self.grid.squares if len(values[s]) > 1)
        return self.__return_some_value(self.__search
                                          (self.__eliminate_other_value
                                           (values.copy(), s, d))
                    for d in values[s])
      
    
    def __return_some_value(self,seq):
        '''This method returns some element of seq that is true.'''
        for e in seq:
            if e: return e
        return False