""" setup.py """
import os
from setuptools import setup, find_packages

def get_description():
    """ Makes README file into a string"""
    with open("README.rst") as file:
        long_description = file.read()
    return long_description

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

def get_version():
    """ Gets version from impyute.__init__.py

    Runs `impyute.__init__` and loads defined variables into scope
    """
    with open(os.path.join('impyute', '__init__.py')) as version_file:
        # pylint: disable=exec-used, undefined-variable
        exec(version_file.read(), globals())
        return __version__


setup(
    name='impyute',
    author='Elton Law',
    author_email='eltonlaw296@gmail.com',
    version=get_version(),
    url="http://impyute.readthedocs.io/en/latest/",
    download_url='https://github.com/eltonlaw/impyute',
    description='Cross-sectional and time-series data imputation algorithms',
    long_description=get_description(),
    packages=find_packages(exclude=['docs']),
    install_requires=parse_requirements("requirements/common.txt"),
    keywords='imputation',
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering'],
    extras_require={
        'dev': ['pylint', 'sphinx'],
        'test': [],
    },
    license='GPL-3.0'
)
