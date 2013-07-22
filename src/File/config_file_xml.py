'''This class create new xml file'''
import os
from File.config_file import Configfile
from xml.dom import minidom
from xml.dom.minidom import parse

class Xmlfile(Configfile):

    def __init__(self, name,path):
        ''' Start the attributes for xml_file also create the xml 
        configuration file when it does not exist'''
        Configfile.__init__(self, name, path)
        self.file_path=self.path+self.name+".xml"
        if not os.path.isfile("c:\\sudoku\\config\\xml_config_file.xml"):
            self.ensure_dir("c:\\sudoku\\config\\")
            self.ensure_dir("c:\\sudoku\\save\\")
            self._create_xml_config_file()
        self.doc_xml=parse(self.file_path)
            
    def _create_xml_config_file(self):
        '''Create the object'''
        implementacion_DOM = minidom.getDOMImplementation()
        xml_document = implementacion_DOM.\
        createDocument(None, "Sudoku_game", None)
        main_document = xml_document.documentElement
        nodo_main = xml_document.createElement("Settings_SUDOKU")

        nodo_main\
        .appendChild(self.add_element(xml_document, "solver_output_type",\
                                       "Display by console"))
        nodo_main\
        .appendChild(self.add_element(xml_document, "default_algorithm",\
                                       "Norvig"))
        nodo_main.appendChild(self.add_element(xml_document,\
                                                "difficulty_level", "Easy"))
        nodo_main\
        .appendChild(self.add_element(xml_document, \
                                      "save_game", "c:\\sudoku\\save\\"))
        nodo_main.appendChild(self.add_element(xml_document, \
                                               "save_game_number", "10"))

        main_document.appendChild(nodo_main)            
        xml_file = open(self.file_path, "w")  
        xml_document.writexml(xml_file, encoding='utf-8')
        xml_file.close()
        return self.file_path


    def get_xml_value(self, tag_name):
        '''Read the default solver output type, algorithm and difficulty \
        levels from the xml configuration file'''
        for n in self.doc_xml.getElementsByTagName(tag_name):
            value= n.firstChild.data 
        return value
    
    def set_xml_value(self, new_value, tag_name):
        '''Modify the default solver output type, algorithm and difficulty\
         levels from the xml configuration file'''
        node = self.doc_xml.getElementsByTagName(tag_name)
        node[0].firstChild.nodeValue = new_value
        xml_file = open(self.file_path, "w")
        self.doc_xml.writexml(xml_file, encoding='utf-8')
        xml_file.close()
        return node[0].firstChild.nodeValue
    

    def add_element(self, xml_document, element, value):
        '''Add values to the xml configuration file'''
        element_added = xml_document.createElement(element)
        element_added.appendChild(xml_document.createTextNode(value))
        return element_added
    