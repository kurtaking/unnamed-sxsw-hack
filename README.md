# unnamed-sxsw-hack

### Django Project

1. Make sure you have [`virtualenv`] (https://virtualenv.readthedocs.org/en/latest/)
2. `cd sxsw`
3. Create a new virtual environment via `virtualenv venv`
4. Activate virtual environment with `source venv/bin/activate`
5. Install dependencies with `pip install -r requirements.txt` (This may take a few minutes)
6. Run `python manage.py migrate` and ensure no errors come up.
7. To run locally, type `python manage.py runserver` and navigate to the [index page] (http://localhost:8000/)