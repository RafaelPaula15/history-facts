## History-facts

This is the link to open and view the app already deployed. --> https://history-facts-app.herokuapp.com/

Numbers web API: http://numbersapi.com  : is the API we're using to make requests.

To get this application running, make sure you do the following in the Terminal:

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `createdb spotify-playlist`
5. `flask run`
6. `to test post routes uncomment this line on app.py --> app.config['WTF_CSRF_ENABLED'] = False`
7. `run this line from your terminal to test --> python3 -m unittest test_app.py`


### What this application does:

Users can enter a number(a year) between 1 to 2022.
Next, user will get back an interesting fact about that year.
In the facts page, users will be able to see the last 10 requests made.
There's also an edit button where users can add or edit a personal note.
And there're a delete which would delete a year along with its fact.
For this application facts about any year and notes are being saved in a database.
And there is another database to test the application.
It is also posible to enter the same year more then one time and get a different fact.


### To build this application I used the following :
1. `Python3`
2. `Flaks`
3. `PostgreSQL`
3. `SQLAlchemy`
4. `WTForms`
5. `Requests`





