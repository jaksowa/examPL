# Setup

To set up the virtual enviroment, run

    $ python3 -m venv .venv

To activate the created virtual environment, run

    $ source .venv/bin/activate

Depending on your system, the activation of the virual environment might be
different (see https://docs.python.org/3/library/venv.html#how-venvs-work)

To install the dependencies, run

    (.venv) $ pip install -r requirements.txt


# Testing

To execute the tests, run

    (.venv) $ pytest
