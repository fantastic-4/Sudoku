

import sys
sys.path.append("../src")
from coverage import coverage

cov=coverage(omit=['*__.py', '*test*.py'])
cov.start()
import unittest

from UnitTests.test_config_file_xml import Test_XML_config_file
from UnitTests.test_grid import Test_grid
from UnitTests.test_csv_file import Test_csv_file
from UnitTests.test_txt_file import Test_txt_file
from UnitTests.test_brute import Test_Brute
from UnitTests.test_norvig import Test_norvig
from UnitTests.test_display import Test_Display
from UnitTests.test_DLX import TestDlxMatrix
from UnitTests.test_integration1_using_both_algorithms import Test_integration_using_norvig
from UnitTests.test_sudoku_game import Test_SudokuGame
from UnitTests.test_validator import Test_validator
# from UnitTests.test_read_xml_config_file import Test_read_the_default_settings_from_an_XML_config_file


if __name__=="__main__":


    suite=unittest.TestSuite()
    
    suite.addTest(unittest.makeSuite(Test_grid))
    suite.addTest(unittest.makeSuite(Test_XML_config_file))
    suite.addTest(unittest.makeSuite(Test_csv_file))
    suite.addTest(unittest.makeSuite(Test_txt_file))
    suite.addTest(unittest.makeSuite(Test_Brute))
    suite.addTest(unittest.makeSuite(Test_norvig))
    suite.addTest(unittest.makeSuite(Test_Display))
    suite.addTest(unittest.makeSuite(TestDlxMatrix))
    suite.addTest(unittest.makeSuite(Test_integration_using_norvig)) 
    suite.addTest(unittest.makeSuite(Test_SudokuGame))   
    suite.addTest(unittest.makeSuite(Test_validator))
#     suite.addTest(unittest.makeSuite(Test_read_the_default_settings_from_an_XML_config_file))


    unittest.TextTestRunner(verbosity=6).run(suite)
    cov.stop()
    cov.html_report(directory='covhtml')
#medir la cantidad de codigo q usan los unittests
#usar coverage.py    