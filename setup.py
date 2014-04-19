from distutils.core import setup

setup(name='pbf_salesforce',
      version='.2',
      description="Programmer's Best Friend Utility Extension for Salesforce",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf_salesforce', 'pbf_salesforce.Commands', 'pbf_salesforce.helpers', 'pbf_salesforce.templates'],
      #package_data = {'pbf_salesforce.templates':[]}, # Add template files
     )