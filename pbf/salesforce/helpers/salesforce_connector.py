from pbf.salesforce.helpers.salesforce_project_helper import GetCurrentSalesforceProject

from simple_salesforce import Salesforce

class SalesforceConnector:
    """ Represents a connector to perform calls to the Salesforce server """
    
    def __init__(self):
        """ Initialize the Salesforce Connector """
        project = GetCurrentSalesforceProject()
        self.sfConnection = Salesforce(username='cloew123@gmail.com', password='BlahBlah123', security_token='XAPGsrqELnLSgLwhb76knrRZV')
        
    def query(self, queryString):
        """ Perform a SOQL query """
        return self.sfConnection.query(queryString)['records']
    
    def save(self, filename):
        """ Save the given file as the proper Apex Type """
        with open(filename, 'r') as file:
            className = filename.split('.')[0]
            lines = file.readlines()
            classBody = "".join(lines)
            existingClass = self.query("SELECT Id FROM ApexClass Where Name='{0}'".format(className))
            
            if len(existingClass) > 0:
                print "Updating Existing Class"
                self.saveExisting(existingClass[0]['Id'], classBody)
            else:
                print "Saving New Class"
                self.saveNew(className, classBody)
    
    def saveNew(self, className, classBody):
        """ Save a brand new class """
        self.sfConnection.ApexClass.create({'Name':className, 'Body':classBody})
        
    def saveExisting(self, classId, classBody, metadataContainerId=None):
        """ Save a brand new class """
        containerName = 'PySF Metadata Container'
        metadataContainers = self.query("SELECT Id FROM MetadataContainer WHERE Name = '{0}'".format(containerName))
        if len(metadataContainers) > 0:
            self.sfConnection.MetadataContainer.delete(metadataContainers[0]['Id'])
        metadataContainerId = self.sfConnection.MetadataContainer.create({'Name':containerName})['id']
        self.sfConnection.ApexClassMember.create({'ContentEntityId':classId, 'Body':classBody, 'MetadataContainerId':metadataContainerId})
        
        requestId = self.sfConnection.ContainerAsyncRequest.create({'MetadataContainerId':metadataContainerId})['id']
        request = self.query("SELECT CompilerErrors, ErrorMsg, State FROM ContainerAsyncRequest WHERE Id='{0}'".format(requestId))[0]
        
        while request['State'] == 'Queued':
            print "Waiting"
            request = self.query("SELECT CompilerErrors, ErrorMsg, State FROM ContainerAsyncRequest WHERE Id='{0}'".format(requestId))[0]
            
        print "State:", request['State']
        print "Compile Errors:", request['CompilerErrors']
        print "Error Message:", request['ErrorMsg']