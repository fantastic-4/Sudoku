from Parser.grid import Grid
def input_grid():
    '''
    Function to input a Sudoku grid from keyboard.
    '''
    print("\n***** Input Sudoku Grid *****")
    print("\nInstructions:\n")
    print("1) Enter 81 numbers and press Enter key.")
    print("2) Use '0' or '.' to make reference to empty slots.")
    print("3) Press Enter key, before complete the 81 numbers, to fill the rest with empty slots.")
    print("4) Only Numbers are allowed, at any error you will be prompted to start again")
    print("5) To exit this option enter 'q'\n")
    
    flag = False
    while not flag:
        input_text = raw_input("Start to enter numbers: ")
        if(input_text in "qQ"): break
        input_text,flag = __validate_text__(input_text)
    if(flag): print input_text
    
def __validate_text__(text):
    '''
    Function to validate the grid and if it is valid and its size is not 81 characters,
    then it will be completed wit '0'.
    :param text: text with characters to be used on Sudoku grid.
    '''
    while(len(text) < 81): text += "0"
    grid = Grid()
    flag = grid.validate_grid(text)
    if(not flag):
        print("ERROR, Invalid input content.")
    return text,flag