# smart-suction

Repository for evaluating data collected for the smart suction cup project.

# dev guide

Do the following commands in this directory.

- Upgrade pip `python -m pip install --upgarde pip`
- Initialize a python virtual environment `python -m venv [virtual environment name]`
- Activate the virtual environment
  - Windows `.\[virtual env name]\Scripts\activate`
  - Linux\OSX `.\[virtual env name]\bin\activate`
- Install requirements `python -m pip install -r requirements.txt`
- Install this package in editable mode (for pytest and relative imports) `pip install -e .`

The structure of `src\smart-suction` should be identical to the structure of `tests\`, following the convention found [here](https://docs.pytest.org/en/stable/explanation/goodpractices.html#tests-outside-application-code).
