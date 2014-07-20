from pbf.Commands import command_manager
from pbf.helpers.filename_helper import GetBaseFilenameWithoutExtension
from pbf.templates import template_manager

from pbf_salesforce.templates import TemplatesRoot

class NewClass:
    """ Command to create a new class """
    category = "new"
    command = "class"
    description = "Creates a new Apex Class"
    
    templateFile = 'new_class.cls'
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new Apex class')
    
    def run(self, args):
        """ Run the command """
        filepath = args[0]
        print "Creating Apex Class at:", filepath
        self.createClass(filepath)
        
    def createClass(self, filepath):
        """ Create a Class """
        keywords = {'%ClassName%':GetBaseFilenameWithoutExtension(filepath)}
        template_manager.CopyTemplate(filepath, self.templateFile, keywords, TemplatesRoot)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/class]".format(category=self.category, command=self.command)
        print "Creates an Apex Class the path given"
    
command_manager.RegisterCommand(NewClass)