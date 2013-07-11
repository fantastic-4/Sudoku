from Main.validate import Validate
def input_function():
    print("\n***** Input Sudoku Game *****")
    print("\nInstructions:\n")
    print("1) Enter 81 numbers and press Enter key.")
    print("2) Use '0' or '.' to make reference to empty slots.")
    print("3) Press Enter key, before complete the 81 numbers, to fill the rest with empty slots.")
    print("4) Only Numbers are allowed, at any error you will be prompted to start again")
    print("5) To exit this option press Escape key\n")
    
    while True:
        input_text = str(raw_input("Start to enter numbers: "))
        input_text = validate_text(input_text)
        if(input_text != ""): break
    
    validate = Validate()
    if(validate.validate_values(input_text)):
        print (input_text)
    else: print("ERROR, Invalid input content.")
    
'''This function could be moved to Validate class.'''
def validate_text(text):
    while(len(text) < 81): text += "0"
    return text