# World of Сalculators
A website contains various mathematical calculators written in Python using Django framework.<br />
The site was developed as part of a training course.<br />
<br />
**Author:** Ammosov Yaroslav<br />
**Website Language:** Russian<br />
**Timezone:** Moscow<br />

## Launching
1. Clone/download this repository
2. Install all dependencies from `environment.yml` file. For conda:<br />
`conda env create -f environment.yml`
3. Launch the Django server using:<br />
`make runserver`

## Dependencies and tools
This website uses:<br />
1. **conda** environment, however you can install packages from `environment.yml` file to any environment.
2. **make** system for short commands to test and run the code
3. **Django** as web framework
4. **sqlite3** as database mangement system
5. **Bootstrap** as design system
6. **Pytest** as testing/coverage tool
7. **Pylint**, **MyPy** and **flake8** as linters
8. [**simpeeval**](https://github.com/danthedeckie/simpleeval) as secure replacement for `eval` function

## Code Testing
* To lint, test and run project use:<br />
`make all`

* To lint project use:<br />
`make lint`

* To test project via pytest use:<br />
`make test`

## Screenshots and Demonstration
### Main page
You can choose calculator and access history of calcultions on main page.<br />
There are two calculators available now:<br />
1. Regular (text form) calculator
2. Quadratic equations calculator
![index](https://github.com/CONDUCTOR77747/calc_world/assets/55601049/cef896d7-543e-4569-9b15-ce6506486875)

### Regular calculator
On this page you can enter your expression:
![regular_calc](https://github.com/CONDUCTOR77747/calc_world/assets/55601049/35d1464b-217a-4bff-93aa-fedd943855a9)

After pressing submit button the result page will show up and you can save your calculation to history by pressng the button:
![regular_calc_result](https://github.com/CONDUCTOR77747/calc_world/assets/55601049/64f91a5b-cca8-4012-8be3-221b3d28141e)

#### Input validation
There are some examples of invalid input:
![regular_calc_error1](https://github.com/CONDUCTOR77747/calc_world/assets/55601049/bd830715-a73f-4d69-a587-aca9dfae0f8e)
![regular_calc_error2](https://github.com/CONDUCTOR77747/calc_world/assets/55601049/d45627c2-5f5c-4bfa-8077-34a669619a42)
![regular_calc_error3](https://github.com/CONDUCTOR77747/calc_world/assets/55601049/15d8eeb5-da6d-456a-af71-b1e9d0107153)

### Quadratic equations calculator
You can enter coefficients:
![quadratic_calc](https://github.com/CONDUCTOR77747/calc_world/assets/55601049/d50c39ac-2b04-4b4a-9951-935b2f5b2573)
After pressing submit button the result will show up:
![quadratic_calc_result](https://github.com/CONDUCTOR77747/calc_world/assets/55601049/76056441-1122-403a-b016-be9de13403d1)

#### Input validation
##### Invalid input
Example of invalid input:
![quadratic_calc_error](https://github.com/CONDUCTOR77747/calc_world/assets/55601049/65dd963f-20a9-4f59-b052-b0c3bfc33d16)

##### Valid input
Few valid input examples:
![quadratic_calc_valid1](https://github.com/CONDUCTOR77747/calc_world/assets/55601049/a9bcc37b-d52c-4044-972e-1aa4813e27a7)
![quadratic_calc_valid2](https://github.com/CONDUCTOR77747/calc_world/assets/55601049/575008a8-683c-4abd-95de-27d658aea809)


