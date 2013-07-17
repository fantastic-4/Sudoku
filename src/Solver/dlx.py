import string
import cStringIO
import math
from Parser.grid import Grid

ROOTNODE = 0
LEFT   = 0
RIGHT  = 1
UP     = 2
DOWN   = 3
COLUMN = 4
INDEX  = 5
COUNT  = 5

class DLX:
    def __init__(self):
        self.sizes = {4: [2, 2], 6: [2, 3], 8: [2, 4], 9: [3, 3],
                      10: [2,5], 12:[3, 4], 15: [3, 5], 16: [4, 4],
                      20: [4, 5], 24: [4, 6], 25: [5, 5], 28: [4, 7],
                      30: [5, 6], 32: [4, 8], 35: [5, 7], 36: [6, 6]}
        self.chartable = string.maketrans(
            ".0123456789",
            "\x00" + "".join(map(chr, xrange(0,10))))
        self.sarray = [0]*81
        self.blockrows = 3
        self.blockcols = 3
        self.grid=Grid()

    def __init_matrix(self):
        self.cursolution = []
        self.solutioncallback = None
        self.nodes = [[0, 0, None, None, None, None]]  
    def __walknodes(self, firstnode, direction):
        '''Generator for iterating over all nodes in given direction
        (not including firstnode).'''
        nodetable=self.nodes
        n = nodetable[firstnode][direction]
        while n != firstnode:
            yield n
            n = nodetable[n][direction]
    def __constructmatrix(self, ones, initialsolution=[]):
        '''Construct the (sparse) DLX matrix based on list "ones"'''
        self.cursolution = []
        self.nodes = [[ROOTNODE, ROOTNODE, None, None, None, None]]
        nodetable = self.nodes
        ones.sort()
        pruneNodes = []
        headers = [ROOTNODE] # indexes of header nodes for faster access
        for r in ones:
            curRow = r[0]  # row index
            columns = r[1] # column indexes
            if len(columns) == 0: continue
            columns.sort()
            while len(headers) <= columns[-1]:
                lastheader = headers[-1]
                newind = len(nodetable)
                nodetable.append([lastheader, ROOTNODE, newind, newind, None, 0])
                nodetable[ROOTNODE][LEFT] = newind
                nodetable[lastheader][RIGHT] = newind
                headers.append(newind)
            newind = len(nodetable)
            for i, c in enumerate(columns):
                h = headers[c]
                l = newind + ((i-1) % len(columns))
                r = newind + ((i+1) % len(columns))
                nodetable.append([l, r, nodetable[h][UP], h, h, curRow])
                nodetable[nodetable[h][UP]][DOWN] = newind+i
                nodetable[h][UP] = newind+i
                nodetable[h][COUNT] += 1
            if curRow in initialsolution:
                pruneNodes.append(newind)
        for n in pruneNodes:
            self.cursolution += [nodetable[n][INDEX]]
            self.__covercolumn(nodetable[n][COLUMN])
            for j in self.__walknodes(n, RIGHT):
                self.__covercolumn(nodetable[j][COLUMN])

    def __covercolumn(self, c):
        '''Cover the correct column of the matrix DLX'''
        nodetable = self.nodes
        nodetable[nodetable[c][RIGHT]][LEFT] = nodetable[c][LEFT]
        nodetable[nodetable[c][LEFT]][RIGHT] = nodetable[c][RIGHT]
        for i in self.__walknodes(c, DOWN):
            for j in self.__walknodes(i, RIGHT):
                nodetable[nodetable[j][DOWN]][UP] = nodetable[j][UP]
                nodetable[nodetable[j][UP]][DOWN] = nodetable[j][DOWN]
                nodetable[nodetable[j][COLUMN]][COUNT] -= 1

    def __uncovercolumn(self, c):
        '''Uncover the correct column of the matrix DLX'''
        nodetable = self.nodes
        for i in self.__walknodes(c, UP):
            for j in self.__walknodes(i, LEFT):
                nodetable[nodetable[j][DOWN]][UP] = j
                nodetable[nodetable[j][UP]][DOWN] = j
                nodetable[nodetable[j][COLUMN]][COUNT] += 1
        nodetable[nodetable[c][RIGHT]][LEFT] = c
        nodetable[nodetable[c][LEFT]][RIGHT] = c

    def __dosearch(self):
        '''Internal. The actual recursive searching function.'''
        nodetable = self.nodes # optimization: local variables are faster
        if nodetable[ROOTNODE][RIGHT] == ROOTNODE:
            if self.solutioncallback is not None:
                self.solutioncallback(self.cursolution)
                return None
            else:
                return self.cursolution
        a = None
        c = nodetable[ROOTNODE][RIGHT]
        maxcount = nodetable[nodetable[ROOTNODE][RIGHT]][COUNT]
        for j in self.__walknodes(ROOTNODE, RIGHT):
            if nodetable[j][COUNT] < maxcount:
                c = j
                maxcount = nodetable[j][COUNT]
        self.__covercolumn(c)
        for r in self.__walknodes(c, DOWN):
            self.cursolution += [nodetable[r][INDEX]]
            for j in self.__walknodes(r, RIGHT):
                self.__covercolumn(nodetable[j][COLUMN])
            a = self.__dosearch()
            if a is not None: return a
            self.cursolution = self.cursolution[:-1]
            for j in self.__walknodes(r, LEFT):
                self.__uncovercolumn(nodetable[j][COLUMN])
        self.__uncovercolumn(c)
        return None

    def solve_dlx(self, ones, initialsolution=[], callback=None):
        '''Construct DLX matrix and solve exact cover problem. Returns
        list of row indexes of found solution or None none is found.'''

        self.__constructmatrix(ones, initialsolution)
        self.solutioncallback=callback
        
        return  self.__dosearch()

    '''Create the Matrix Sudoku with DLX format '''
    def __convert_the_array_to_string(self):
        '''Convert the array to a string list'''
        ret = cStringIO.StringIO()
        for i in xrange(len(self.sarray)):
            ret.write(str(self.sarray[i])) 
        return ret.getvalue()
    def convert_to_array(self, s):
        '''convert the string to a array'''
        sudokustring = s
        boardsize = int(math.sqrt(len(sudokustring)))
        self.blockrows, self.blockcols = self.sizes[boardsize]
        self.sarray = map(ord, string.translate(sudokustring, self.chartable))
        return self.sarray

    def __get_solution_matrix_dlx__(self):
        '''generate the DLX matrix with rows and columns for sudoku game 
        i.e for a game of 9 x 9, it generate 729 rows and 324 columns and also
        given the solution for sudoku game'''
        br = self.blockrows
        bc = self.blockcols
        puzzlerows = br*bc         # number of rows in the puzzle
        puzzlecols = puzzlerows    # number of columns in the puzzle
        digits = puzzlerows        # max digit
        bl = puzzlerows*puzzlecols # board length
        givenrows = []
        dlxones = []
        for r in xrange(0, puzzlerows):
            for c in xrange(0, puzzlecols):
                for d in xrange(0, digits):
                    dlxrow = bl*r + puzzlerows*c + d + 1
                    if self.sarray[puzzlecols*r+c]-1 == d:
                        givenrows.append(dlxrow)
                    box = br*(r/br)+c/bc
                    dlxones.append([dlxrow,
                                    [puzzlecols*r+c+1,      # <r,c> constrain
                                     bl+digits*r+d+1,       # <d,r>
                                     2*bl+digits*c+d+1,     # <d,c>
                                     3*bl+digits*box+d+1]]) # <d,b>
        self.__init_matrix()
        self.nsolutions = 0
        solution = self.solve_dlx(dlxones, givenrows)
        
        if solution is not None:
            return self.__getsolution__(solution)

    def __getsolution__(self, solution):
        '''Sort the array with the solution'''
        br = self.blockrows
        bc = self.blockcols
        puzzlerows = br*bc         # number of rows in the puzzle
        puzzlecols = puzzlerows    # number of columns in the puzzle
        digits = puzzlerows        # max digit
        bl = puzzlerows*puzzlecols # board length
        self.nsolutions += 1
        for s in solution:
            d = (s-1) % digits + 1
            c = ((s-1)/digits) % puzzlecols
            r = (s-1)/bl
            self.sarray[puzzlecols*r+c] = d
        return self.__convert_the_array_to_string()
    def solve(self, dictionary):
        self.convert_to_array(self.__convert_dict_to_a_string(dictionary))
        string=self.__get_solution_matrix_dlx__()
        return self.grid.set_values(string)
             
    def __convert_dict_to_a_string(self,dictionary):
        '''this method receives the dict and then convert to a string'''
        new_string = ""
        rows = "ABCDEFGHI"
        columns = "123456789"
        for row in rows:
            for column in columns:
                new_string += dictionary[row + column]
        return new_string
        