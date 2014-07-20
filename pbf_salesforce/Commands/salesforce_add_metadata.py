from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory
from pbf.helpers.Project.project_xml_helper import SaveProjectXML

from pbf.Commands import command_manager

from xml.etree.ElementTree import SubElement

class SalesforceAddMetadata:
    """ Add Salesforce metadata to a Project """
    category = "salesforce"
    command = "add-metadata"
    description = "Add Salesforce metadata to the current project"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('username', action='store', help='Salesforce Organizaation Username')
        parser.add_argument('password', action='store', help='Salesforce Organizaation Password')
        parser.add_argument('token', action='store', help='Salesforce Organizaation Security Token')
    
    def run(self, arguments):
        """ Run the command """
        username = arguments.username
        password = arguments.password
        securityToken = arguments.token
        project = GetParentProjectFromDirectory()
        
        if project is None:
            print "No project for current directory"
        else:
            self.addSalesforceMetadata(project, username, password, securityToken)
            
    def addSalesforceMetadata(self, project, username, password, securityToken):
        """ Add Salesforce Metadata to the project XML """
        salesforceElement = SubElement(project.projectXML, "salesforce")
        usernameElement = SubElement(salesforceElement, "username")
        usernameElement.text = username
        passwordElement = SubElement(salesforceElement, "password")
        passwordElement.text = password
        securityTokenElement = SubElement(salesforceElement, "securityToken")
        securityTokenElement.text = securityToken
        
        SaveProjectXML()
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [username] [password] [security token]".format(category=self.category, command=self.command)
        print "Add Salesforce Credentials to existing project"
    
command_manager.RegisterCommand(SalesforceAddMetadata)