# Contributing

The following is a set of guidelines for contributing to the imputations library, impyute, which is hosted [here](https://github.com/eltonlaw/impyute) 
1. Check for open [issues](https://github.com/eltonlaw/impyute/issues) or create a new one to discuss new features or bugs.
2. Fork the repo on [github](https://github.com/eltonlaw/impyute) and make the changes.
3. Write a test to show that the bug was fixed/feature works 
4. Submit your pull request and reference the issue and add yourself to [AUTHORS](https://github.com/eltonlaw/impyute/blob/master/AUTHORS.rst)!

### Suggesting Enhancements

This project was created to cover everything required in the step of your workflow where you move from data with missing values to data without missing values. Simple enough right? Any enhancement that brings value with that in mind are welcome. 

### Development

The unit testing framework used is just the basic `unittest` prepackaged with Python. To run tests:

    $ python -m unittest discover

Use [.pylintrc](https://github.com/eltonlaw/impyute/blob/master/.pylintrc) to lint files. You need pylint installed; [install pylint](https://www.pylint.org/#install)

    $ pylint --rcfile=.pylintrc impyute/

### Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.
