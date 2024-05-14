# World of Сalculators
A website contains various mathematical calculators written in Python using Django framework.
The site was developed as part of a training course.

## Launching
1. Install all dependencies from `environment.yml` file. For conda:
`conda env create -f environment.yml`
2. Launch the Django server using:
`make runserver`

## Code Testing
To lint project use:
`make lint`

To test project via pytest use:
`make test`

To lint, test and run project use:
`make all`
