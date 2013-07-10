import os
from File.config_file import Config_file
from xml.dom import minidom
from xml.dom.minidom import parse

class Xml_file(Config_file):
    """doc string for xml_file"""
    def __init__(self, name,path):
        Config_file.__init__(self, name, path)
        self.file_path=self.path+self.name+".xml"
        if not os.path.isfile("../File/xml_config_file"):
            self._create_xml_config_file()
        
        self.doc_xml=parse(self.file_path)
        #self.implementacion_DOM = minidom.getDOMImplementation() # Create object DOM
        
    """Creating a xml file if it doesn't exist then the xml file is created"""    
    def _create_xml_config_file(self):
        # Create the object Document.
        implementacion_DOM = minidom.getDOMImplementation()
        xml_document = implementacion_DOM.createDocument(None, "Sudoku_game", None)
        raiz_documento = xml_document.documentElement
        nodo_main = xml_document.createElement("Settings_SUDOKO")

        # Adding the elements to node.
        nodo_main.appendChild(self.add_element(xml_document, "solver_output_type", "Consola"))
        nodo_main.appendChild(self.add_element(xml_document, "default_algorithm", "Norvig"))
        nodo_main.appendChild(self.add_element(xml_document, "difficulty_level", "Easy"))

        # adding the node.
        raiz_documento.appendChild(nodo_main)            
        
        # opening the xml file and writing the data
        xml_file = open(self.file_path, "w")  
        xml_document.writexml(xml_file, encoding='utf-8')
        xml_file.close()
        return self.file_path

    """Read the solver output type, default algorithm and difficulty levels from a xml file"""

    def get_xml_value(self, tag_name):
        for n in self.doc_xml.getElementsByTagName(tag_name):
            value= n.firstChild.data
        return value
    
    def set_xml_value(self, new_value, tag_name):
        node = self.doc_xml.getElementsByTagName(tag_name)
        node[0].firstChild.nodeValue = new_value
        xml_file = open(self.file_path, "w")
        self.doc_xml.writexml(xml_file, encoding='utf-8')
        xml_file.close()
        return node[0].firstChild.nodeValue
        
    def add_element(self, xml_document, element, value):
        element_added = xml_document.createElement(element)
        element_added.appendChild(xml_document.createTextNode(value))
        return element_added