

import sys
sys.path.append("../src")
from coverage import coverage

cov=coverage(omit=['*__.py', '*test*.py'])
cov.start()
import unittest

from UnitTests.test_config_file_xml import TestXMLconfigfile
from UnitTests.test_grid import Test_grid
from UnitTests.test_csv_file import TestCsvFile
from UnitTests.test_txt_file import Testtxtfile
from UnitTests.test_brute import Test_Brute
from UnitTests.test_norvig import Test_norvig
from UnitTests.test_display import Test_Display
from UnitTests.test_DLX import TestDlxMatrix
from UnitTests.test_integration1_using_both_algorithms import Test_integration_using_norvig
from UnitTests.test_sudoku_game import Test_SudokuGame
from UnitTests.test_validator import Test_validator
from UnitTests.Test_play_sudoku import TestPlaySudoku
from UnitTests.test_bugs_found import TestBugFound


if __name__=="__main__":


    suite=unittest.TestSuite()
    
    suite.addTest(unittest.makeSuite(Test_grid))
    suite.addTest(unittest.makeSuite(TestXMLconfigfile))
    suite.addTest(unittest.makeSuite(TestCsvFile))
    suite.addTest(unittest.makeSuite(Test_Brute))
    suite.addTest(unittest.makeSuite(Test_norvig))
    suite.addTest(unittest.makeSuite(Test_Display))
    suite.addTest(unittest.makeSuite(TestDlxMatrix))
    suite.addTest(unittest.makeSuite(Test_integration_using_norvig)) 
    suite.addTest(unittest.makeSuite(Test_validator))
    suite.addTest(unittest.makeSuite(TestPlaySudoku))
    suite.addTest(unittest.makeSuite(Test_SudokuGame))
    suite.addTest(unittest.makeSuite(Testtxtfile))
    suite.addTest(unittest.makeSuite(TestBugFound))
#     suite.addTest(unittest.makeSuite(Test_read_the_default_settings_from_an_XML_config_file))


    unittest.TextTestRunner(verbosity=6).run(suite)
    cov.stop()
    cov.html_report(directory='covhtml')
#medir la cantidad de codigo q usan los unittests
#usar coverage.py    