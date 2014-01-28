
class SalesforceProject:
    """ Represents a salesforce project """
    
    def __init__(self, project):
        """ Initialize the Salesforce Project """
        self.project = project
        self.salesforceXML = self.project.projectXML.find('salesforce')
        
    @property
    def username(self):
        """ Return the Project Username """
        return self.salesforceXML.find('username').text
        
    @property
    def password(self):
        """ Return the Project Password """
        return self.salesforceXML.find('password').text
        
    @property
    def securityToken(self):
        """ Return the Project Securtiy Token """
        return self.salesforceXML.find('securityToken').text