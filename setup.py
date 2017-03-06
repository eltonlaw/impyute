""" setup.py """
from setuptools import setup, find_packages
from pip.req import parse_requirements

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

parsed_reqs = parse_requirements("requirements.txt", session=False)
reqs = [str(ir.req) for ir in parsed_reqs]

setup(name='impy',
      author='Elton Law',
      author_email='eltonlaw296@gmail.com',
      version='0.1',
      url='https://github.com/eltonlaw/impy',
      description='Library of the different imputation algorithms; methods for \
      dealing with ambiguity and handling missing data.',
      long_description=LONG_DESCRIPTION,
      packages=find_packages(exclude=['docs']),
      install_requires=reqs,
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python',
                   'Topic :: Software Development',
                   'Topic :: Scientific/Engineering'],
      test_suite="nose.collector",
      tests_require=["nose"],
      license='GPL-3.0')
