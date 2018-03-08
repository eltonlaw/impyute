# Contributing

Hey thanks for deciding to contribute!

The following is a set of guidelines for contributing to the imputations library, impyute, which is hosted [here](https://github.com/eltonlaw/impyute) 

1. Check for open [issues](https://github.com/eltonlaw/impyute/issues) or create a new one to discuss new features or bugs.
2. Fork the repo on [github](https://github.com/eltonlaw/impyute) and make the changes. Make sure you follow the guidelines below.
3. Write a unit test to show that the bug was fixed/feature works 
4. Submit your pull request and reference the issue (and add yourself to [AUTHORS](https://github.com/eltonlaw/impyute/blob/master/AUTHORS.rst)!)

### Development

This project was built for Python 3.5 and 3.6. (If you would like to work on extending this to other versions, that would be very welcome.)

Using [Sphinx's autodoc](http://www.sphinx-doc.org/en/stable/ext/autodoc.html) module, docstrings are used as the documentation. Make sure that all docstrings are formatted according to the [NumPy/SciPy Docstring Standard](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt#docstring-standard)

Use [.pylintrc](https://github.com/eltonlaw/impyute/blob/master/.pylintrc) to lint files in accordance with [PEP8](https://www.python.org/dev/peps/pep-0008/). You will first need pylint installed: [install pylint](https://www.pylint.org/#install)

    $ pylint --rcfile=.pylintrc impyute/

Put unit tests in the `test` directory in root. The testing environment works like this: 1) Build a docker image with multiple python versions 2) Run the container with pytest for each python version.

    $ make test

### Suggesting Enhancements

This project was created to cover everything required in the step of your pipeline where you move from data with missing values to data without missing values. Simple enough right? Any enhancements that brings value with that in mind are welcome.

### Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

