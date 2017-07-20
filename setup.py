""" setup.py """
from setuptools import setup, find_packages
from pip.req import parse_requirements

with open("README.rst") as f:
    LONG_DESCRIPTION = f.read()

PARSED_REQS = parse_requirements("requirements.txt", session=False)
REQS = [str(ir.req) for ir in PARSED_REQS]

setup(
    name='impyute',
    author='Elton Law',
    author_email='eltonlaw296@gmail.com',
    version='0.0.4',
    url='https://github.com/eltonlaw/impyute',
    description='Library of cross-sectional and time-series data imputation algorithms along \
                 with some helper functions',
    long_description=LONG_DESCRIPTION,
    packages=find_packages(exclude=['docs']),
    install_requires=REQS,
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
