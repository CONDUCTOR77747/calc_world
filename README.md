# World of Сalculators
A website contains various mathematical calculators written in Python using Django framework.<br />
The site was developed as part of a training course.

## Launching
1. Install all dependencies from `environment.yml` file. For conda:<br />
`conda env create -f environment.yml`
2. Launch the Django server using:<br />
`make runserver`

## Dependencies and tools
This website uses:<br />
1. **conda** environment is recommended, however you can install packages from `environment.yml` file to any environment.
2. **make** system to test and run the code
3. **Django** as web framework
4. **Bootstrap** as design system
5. **Pytest** as testing/coverage tool
6. **Pylint**, **MyPy** and **flake8** as linters
7. [**simpeeval**](https://github.com/danthedeckie/simpleeval) as secure replacement for `eval` function

## Code Testing
To lint, test and run project use:<br />
`make all`

To lint project use:<br />
`make lint`

To test project via pytest use:<br />
`make test`