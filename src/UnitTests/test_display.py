import unittest
from Main.display import Display

class Test_grid(unittest.TestCase):


    def setUp(self):
        self.display=Display()

    def test_the_display_method_in_grid_prints_correct_format(self):
        gridX={'I6': '0', 'H9': '9', 'I2': '0', 'E8': '0', 'H3': '0', 'H7': '0', 'I7': '3', 'I4': '0', 'H5': '0', 'F9': '0', 'G7': '5', 'G6': '9', 'G5': '0', 'E1': '7', 'G3': '2', 'G2': '0', 'G1': '0', 'I1': '0', 'C8': '0', 'I3': '5', 'E5': '0', 'I5': '1', 'C9': '0', 'G9': '0', 'G8': '0', 'A1': '0', 'A3': '3', 'A2': '0', 'A5': '2', 'A4': '0', 'A7': '6', 'A6': '0', 'C3': '1', 'C2': '0', 'C1': '0', 'E6': '0', 'C7': '4', 'C6': '6', 'C5': '0', 'C4': '8', 'I9': '0', 'D8': '0', 'I8': '0', 'E4': '0', 'D9': '0', 'H8': '0', 'F6': '8', 'A9': '0', 'G4': '6', 'A8': '0', 'E7': '0', 'E3': '0', 'F1': '0', 'F2': '0', 'F3': '6', 'F4': '7', 'F5': '0', 'E2': '0', 'F7': '2', 'F8': '0', 'D2': '0', 'H1': '8', 'H6': '3', 'H2': '0', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '0', 'B6': '5', 'B7': '0', 'E9': '8', 'B1': '9', 'B2': '0', 'B3': '0', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '0', 'B8': '0', 'B9': '1', 'D1': '0'}
        gridY='    1 2 3  4 5 6  7 8 9 \n    --------------------\nA:  0 0 3 |0 2 0 |6 0 0 \nB:  9 0 0 |3 0 5 |0 0 1 \nC:  0 0 1 |8 0 6 |4 0 0 \n    ------+------+------\nD:  0 0 8 |1 0 2 |9 0 0 \nE:  7 0 0 |0 0 0 |0 0 8 \nF:  0 0 6 |7 0 8 |2 0 0 \n    ------+------+------\nG:  0 0 2 |6 0 9 |5 0 0 \nH:  8 0 0 |2 0 3 |0 0 9 \nI:  0 0 5 |0 1 0 |3 0 0 \n'
        self.assertEqual(self.display.display(gridX),gridY)
        
     
        
if __name__ == "__main__":
    unittest.main()  