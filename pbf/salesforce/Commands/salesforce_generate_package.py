from pbf.Commands import command_manager
from pbf.helpers.file_helper import IsDirectory
from pbf.helpers.XML.xml_helper import SaveEtreeXMLPrettily

from pbf.templates import template_manager
from pbf.salesforce.templates import TemplatesRoot

from xml.etree.ElementTree import parse, SubElement

import os

class SalesforceGenerateCommand:
    """ Command to generate Salesforce package xml """
    category = "salesforce"
    command = "generate-package"
    description = "Generate default Salesforce Package XML"
    minimumNumberOfArguments = 1
    
    defaultMetadata = {"ApexClass":["*"],
                       "ApexComponent":["*"],
                       "ApexPage":["*"],
                       "ApexTrigger":["*"],
                       "StaticResource":["*"]}
    
    def run(self, args):
        """ Run the command """
        self.generatePackageXML(args[0])
        
    def generatePackageXML(self, destination, metadata=None):
        """ Generate the Package XML at the given destination with the given metadata """
        if metadata is None:
            metadata = SalesforceGenerateCommand.defaultMetadata
        
        if IsDirectory(destination):
            destination = os.path.join(destination, "package.xml")
        
        template_manager.CopyTemplate(destination, "package.xml", templates_directory=TemplatesRoot)
        self.addMetadataElements(destination, metadata)
        
    def addMetadataElements(self, destination, metadata):
        """ Add Metadata XML to the Package.xml file at destination """
        tree = parse(destination)
        commandElement = tree.getroot()
        
        for name in metadata:
            typesElement = SubElement(commandElement, "types")
            for member in metadata[name]:
                membersElement = SubElement(typesElement, "members")
                membersElement.text = member
            namesElement = SubElement(typesElement, "name")
            namesElement.text = name
            
        SaveEtreeXMLPrettily(tree, destination)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/command.xml]".format(category=self.category, command=self.command)
        print "Generate default Salesforce Command XML"
    
command_manager.RegisterCommand(SalesforceGenerateCommand)