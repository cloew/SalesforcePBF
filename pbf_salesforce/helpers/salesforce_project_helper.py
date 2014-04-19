from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory
from pbf_salesforce.helpers.salesforce_project import SalesforceProject

def GetCurrentSalesforceProject():
    """ Get Salesforce Project for the current directory """
    project = GetParentProjectFromDirectory()
    return SalesforceProject(project)