from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.wrappers import PlainRequest

from models import db, connect_db, YearFact
from forms import YearFactForm, NoteForm
import requests
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///history-facts')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret1')

# uncomment this line to test post routes
# app.config['WTF_CSRF_ENABLED'] = False


# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)



# This route makes a request to http://numbersapi.com/{year}/year and retrieve information about a year.
# then and returns home page.

@app.route("/", methods=["Get", "POST"])
def root():
    """Show Homepage."""
    form = YearFactForm()
    if form.validate_on_submit():
       year = form.year.data
       r = requests.get(f'http://numbersapi.com/{year}/year')
       fact = r.text
       flash(f"New fact about the year {year}!")

       new_fact = YearFact(fact=fact, year=year)
       db.session.add(new_fact)
       db.session.commit()
       return redirect("/facts")
    else:   
       return render_template("home.html", form=form)



# Shows all the facts that are saved in the database.

@app.route("/facts", methods=["Get"])
def facts():
    """Show all facts.""" 
    facts = YearFact.query.order_by(YearFact.id.desc()).limit(10).all()
    return render_template("facts.html", facts=facts )     



# Deletes a fact.

@app.route('/facts/<int:id>/delete', methods=["GET", "DELETE"])
def delete_fact(id):
   """delete a fact"""
   fact = YearFact.query.get_or_404(id)

   db.session.delete(fact)
   db.session.commit()
   flash("fact was deleted")

   return redirect("/facts")



# This route allows you to add a new note to a fact or edit an existing note.

@app.route('/facts/<int:id>/edit', methods=["GET", "POST"])
def edit_note(id):
   """edit notes"""
   fact = YearFact.query.get_or_404(id)
   form = NoteForm(obj=fact)
   if form.validate_on_submit():
      fact.note = form.note.data
      db.session.commit()
      flash(f"Your note has been saved!")
      return redirect("/facts")
   else:   
      return render_template("edit_fact.html", fact=fact, form=form)




