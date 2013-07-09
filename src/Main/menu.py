'''
Created on Jul 3, 2013

@author: Arnold Huanca
'''

def errorMessage():
    print "Incorrect input. Please enter a proper option."
    
def solve():
    path = input("\n Please enter the path to read the file and solve a Sudoku game: ")


def play_game():
    pass

def configure_settings():
    pass

def exit_game():
    pass

options = {1: solve, 2: play_game, 3: configure_settings, 4: exit_game}


print "Administration Console for Sudoku Game"
print "======================================"

print "1: Solve"
print "2: Play Sudoku"
print "3: Configure Setting"
print "4: Exit"

num = input("\n Please enter an option: ")
options.get(num, errorMessage)() 