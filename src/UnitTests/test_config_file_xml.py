import os
import unittest
from File.config_file_xml import Xmlfile

class TestXMLconfigfile(unittest.TestCase):

    def setUp(self):
        name_xml_file="xml_config_file"
        path_xml_file="c:\\sudoku\\config\\"
        self.xml=Xmlfile(path_xml_file,name_xml_file)
        self.outputfile="Display by console"
        self.algorithm="Norvig"
        self.level="Easy"
        self.save_game="c:\\sudoku\\save\\"
        self.save_game_number="10"

    def test_if_path_does_not_exit_it_is_created(self):
        new_path="c:\\sudoku\\config\\"
        self.xml.ensure_dir(new_path)
        self.assertTrue(os.path.exists(new_path))

    def test_create_xml_file_should_create_a_xml_file_in_the_correct_path(self):
        expected_result = "c:\\sudoku\\config\\xml_config_file.xml"
        path_of_file_created=self.xml._create_xml_config_file()
        self.assertEqual(expected_result,path_of_file_created)
        
    def test_get_xml_value_for_outputfile(self):
        self.assertEqual(self.outputfile, self.xml.\
                         get_xml_value("solver_output_type"))
     
    def test_get_xml_value_for_algorithm(self):
        self.assertEqual(self.algorithm, self.xml.\
                         get_xml_value("default_algorithm"))
     
    def test_get_xml_value_for_difficulty_level(self):
        self.assertEqual(self.level, self.xml.\
                         get_xml_value("difficulty_level"))
        
    def test_set_xml_value_for_algorithm_from_Norvig_to_Brute(self):
        expected_value = "Brute"
        self.assertEqual(expected_value, self.xml.\
                         set_xml_value("Brute","default_algorithm"))

    def test_set_xml_value_for_save_game_path(self):
        path_save_game=self.xml.get_xml_value("save_game")
        self.assertEqual(self.save_game,path_save_game)

    def test_set_xml_value_for_save_game_number_to_display(self):
        save_game_number=self.xml.get_xml_value("save_game_number")
        self.assertEqual(self.save_game_number,save_game_number)

if __name__=='__main__':
    unittest.main()