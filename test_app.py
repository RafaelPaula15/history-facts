from unittest import TestCase

from app import app
from models import db, YearFact

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///history_facts_test'
app.config['SQLALCHEMY_ECHO'] = False


# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class FactViewsTestCase(TestCase):
    """Tests for views for YearFact."""

    def setUp(self):
        """Add sample fact."""

        YearFact.query.delete()

        fact = YearFact(fact="Hello world", year=1, note="NO NOTE")
        db.session.add(fact)
        db.session.commit()

        self.fact_id = fact.id
        self.fact = fact

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    #  tests the /fact route, the one that shows all facts that are saved in the database.

    def test_list_facts(self):
        with app.test_client() as client:
            resp = client.get("/facts")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Hello world', html)



    # tests the / route or home route. make sure it adds a new fact.

    def test_add_fact(self):
        with app.test_client() as client:
            d = {"fact": "Hello world", "year": 1, "note": "NO NOTE"}
            resp = client.post("/", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Hello world", html)  


    # tests the edit route, where we can add a or edit a note.

    def test_edit_fact(self):
        with app.test_client() as client:
            resp = client.post(f"/facts/{self.fact_id}/edit", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('', html) 



    # tests the delete route.  

    def test_delete_fact(self):
        with app.test_client() as client:
            resp = client.delete(f"/facts/{self.fact_id}/delete", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)