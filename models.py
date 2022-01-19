"""Models for history-facts app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class YearFact(db.Model):
    """YearFact."""

    __tablename__ = "facts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fact = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    note = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<YearFact {self.fact} - {self.year} - {self.note}>"



def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)