from Parser.validator import Validator
def input_function():
    print("\n***** Input Sudoku Game *****")
    print("\nInstructions:\n")
    print("1) Enter 81 numbers and press Enter key.")
    print("2) Use '0' or '.' to make reference to empty slots.")
    print("3) Press Enter key, before complete the 81 numbers, to fill the rest with empty slots.")
    print("4) Only Numbers are allowed, at any error you will be prompted to start again")
    print("5) To exit this option press Escape key\n")
    
    flag = False
    while not flag:
        input_text = raw_input("Start to enter numbers: ")
        if(input_text in "qQ"): break
        input_text,flag = validate_text(input_text)
    if(flag): print input_text
    
'''This function could be moved to Validate class.'''
def validate_text(text):
    while(len(text) < 81): text += "0"
    validator = Validator()
    flag = validator.validate_values(text)
    if(not flag):
        print("ERROR, Invalid input content.")
    return text,flag