from pbf.Commands import command_manager
from pbf_salesforce.Commands.new_class import NewClass

class NewTest(NewClass):
    """ Command to Create a new Apex Test """
    category = "new"
    command = "test"
    description = "Creates a new Apex Test Class"
    
    templateFile = 'new_test.cls'
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new Apex Test class')
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/test]".format(category=self.category, command=self.command)
        print "Creates a new Apex Test Class at the location specified"
    
command_manager.RegisterCommand(NewTest)