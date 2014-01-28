from distutils.core import setup

setup(name='pbf.salesforce',
      version='.1',
      description="Programmer's Best Friend Utility Extension for Salesforce",
      author='', # Add your name here
      author_email='', # Add your e-mail here
      packages=['pbf.salesforce', 'pbf.salesforce.Commands', 'pbf.salesforce.templates'],
      #package_data = {'pbf.salesforce.templates':[]}, # Add template files
     )