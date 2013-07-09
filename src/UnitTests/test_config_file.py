import unittest
from File.config_file import Xml_file

class Test_XML_config_file(unittest.TestCase):

    def setUp(self):
        name_xml_file="xml_config_file"
        path_xml_file='../File/'
        self.xml=Xml_file(name_xml_file,path_xml_file)
        self.outputfile="Consola"
        self.algorithm="Norvig"
        self.level="Easy"
        

    def test_create_xml_file_should_create_a_xml_file_in_the_correct_path(self):
        expected_result = "../File/xml_config_file.xml"
        path_of_file_created=self.xml._create_xml_config_file()
        self.assertEqual(expected_result,path_of_file_created)


    def test_get_xml_value_for_outputfile(self):
        self.assertEqual(self.outputfile, self.xml.get_xml_value("solver_output_type"))
    
    def test_get_xml_value_for_algorithm(self):
        self.assertEqual(self.algorithm, self.xml.get_xml_value("default_algorithm"))
    
    def test_get_xml_value_for_difficulty_level(self):
        self.assertEqual(self.level, self.xml.get_xml_value("difficulty_level"))
       
    
    def test_set_xml_value_for_algorithm_from_Norvig_to_Brute(self):
        expected_value = "Brute"
        self.assertEqual(expected_value, self.xml.set_xml_value("Brute","default_algorithm"))

if __name__=='__main__':
    unittest.main()