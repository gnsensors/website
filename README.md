# website

Step 1:  Create python virtual env:

Navigate into directory and run the following command:

`python/\s -m venv venv`

When this is complete, start the virtual environment

` .\venv\Scripts\activate`

Step 2:  Install Flask:

Run the following command:

`pip install flask`

Step 3:

Set Flask up to run:

`$env:FLASK_APP = "app.py"`
`$env:FLASK_ENV = development`
`flask run`
