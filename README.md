# Canvas-Project
A student-made project to create an area to display recent announcements/surveys/etc on the dashboard.

## Getting started

Create a virtual environment and install the requirements from `requirements.txt`

```
python -m pipenv install requirements.txt
python -m pipenv shell
```

To run any of the example `.py` files in the `EXAMPLES` folder, create a file called `tokens.py` and add strings for `API_URL` and `API_TOKEN` (see the `example_token.py` file)

As an example, to run the `01_get_user_id.py` script, cd into the EXAMPLES directory and run

```
python 01_get_user_id.py
```