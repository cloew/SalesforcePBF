from pbf.helpers.file_helper import IsDirectory
from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory
from pbf.salesforce.helpers.salesforce_project_helper import GetCurrentSalesforceProject

from pbf.templates import template_manager
from pbf.salesforce.templates import TemplatesRoot

from xml.etree.ElementTree import parse, SubElement

import os
    
def GenerateBuildProperties(destination):
    """ Generate ANT Build Properties """
    if IsDirectory(destination):
        destination = os.path.join(destination, "build.properties")
        
    project = GetCurrentSalesforceProject()
    keywords = {"%Username%":project.username,
                "%Password%":project.password,
                "%SecurityToken%":project.securityToken}
    template_manager.CopyTemplate(destination, "build.properties", keywords, templates_directory=TemplatesRoot)
    
def LoadBuildXMLTemplateTree():
    """ Returns the XML Tree for the Build XML template """
    return parse(template_manager.GetRealTemplatePath("build.xml", templates_directory=TemplatesRoot))