from pbf.salesforce.helpers.salesforce_project_helper import GetCurrentSalesforceProject

from simple_salesforce import Salesforce

class SalesforceConnector:
    """ Represents a connector to perform calls to the Salesforce server """
    
    def __init__(self):
        """ Initialize the Salesforce Connector """
        project = GetCurrentSalesforceProject()
        self.sfConnection = Salesforce(username='cloew123@gmail.com', password='BlahBlah123', security_token='XAPGsrqELnLSgLwhb76knrRZV')
    
    def save(self, filename):
        """ Save the given file as the proper Apex Type """
        with open(filename, 'r') as file:
            className = filename.split('.')[0]
            lines = file.readlines()
            classBody = "".join(lines)
            # existingClass = query("SELECT Id FROM ApexClass Where Name='{0}'".format(className), sf)
            
            # if len(existingClass) > 0:
                # print "Updating Existing Class"
                # saveExisting(existingClass[0]['Id'], classBody, sf)
            # else:
            print "Saving New Class"
            self.saveNew(className, classBody)
    
    def saveNew(self, className, classBody):
        """ Save a brand new class """
        self.sfConnection.ApexClass.create({'Name':className, 'Body':classBody})