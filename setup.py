from setuptools import setup

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

setup(name='impy',
      author='Elton Law',
      author_email='eltonlaw296@gmail.com',
      version='0.1',
      url='https://github.com/eltonlaw/impy',
      description='Library of the different imputation algorithms; methods for dealing with ambiguity and handling missing data.',
      long_description=LONG_DESCRIPTION, 
      classifiers=['Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python',
                   'Topic :: Software Development',
                   'Topic :: Scientific/Engineering'],
      license='GPL-3.0')
