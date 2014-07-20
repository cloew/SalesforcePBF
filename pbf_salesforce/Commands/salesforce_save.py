from pbf.Commands import command_manager
from pbf_salesforce.helpers.salesforce_connector import SalesforceConnector

class SalesforceSave:
    """ Command to Save a Salesforce file """
    category = "salesforce"
    command = "save"
    description = "Saves provided salesforce files to the server"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('file', action='append', help='Files to save to the Saleforce server')
    
    def run(self, arguments):
        """ Run the command """
        print "Saving"
        self.save(arguments.file)
        
    def save(self, filenames):
        """ Save the given Salesforce files """
        connector = SalesforceConnector()
        connector.save(filenames[0])
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [file] [file2] [file3]...".format(category=self.category, command=self.command)
        print "Saves the provided Apex files to the associated Salesforce Instance"
    
command_manager.RegisterCommand(SalesforceSave)