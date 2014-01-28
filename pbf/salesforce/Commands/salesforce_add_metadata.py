from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory
from pbf.helpers.Project.project_xml_helper import SaveProjectXML

from pbf.Commands import command_manager

from xml.etree.ElementTree import SubElement

class SalesforceAddMetadata:
    """ Add Salesforce metadata to a Project """
    category = "salesforce"
    command = "add-metadata"
    description = "Add Salesforce metadata to the current project"
    minimumNumberOfArguments = 3
    
    def run(self, args):
        """ Run the command """
        username = args[0]
        password = args[1]
        securityToken = args[2]
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