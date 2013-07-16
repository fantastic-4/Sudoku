import unittest
from File.config_file import Config_file, Xml_file

class Test_read_the_default_settings_from_an_XML_config_file(unittest.TestCase):

  def setUp(self):
    name_xml_file="xml_file"
    path_xml_file="C:\\Sudoko"
    self.xml=Xml_file(name_xml_file,path_xml_file)
    self.outputfile="Consola"
    self.algorith="Norvig"
    self.level="Easy"
    

  def test_create_xml_file_should_create_a_xml_file_in_the_correct_path(self):
 #   result=self.xml.create_xml_file(self.outputfile,self.algorith,self.level)
    print self.xml.read_xml_config_file()
  #  self.assertEqual("C:\\Sudoko\\xml_file.xml",result)

#   def test_values_should_read_the_three_values_from_xml_file(self):
#     three_values=(self.outputfile,self.algorith,self.level)
#     self.assertEqual(three_values,self.xml.read_xml_config_file())


if __name__=='__main__':
	unittest.main()