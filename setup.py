from distutils.core import setup

setup(name='pbf.salesforce',
      version='.1',
      description="Programmer's Best Friend Utility Extension for Salesforce",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf.salesforce', 'pbf.salesforce.Commands', 'pbf.salesforce.helpers', 'pbf.salesforce.templates'],
      #package_data = {'pbf.salesforce.templates':[]}, # Add template files
     )