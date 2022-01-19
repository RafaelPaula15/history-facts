"""seed file to make sample data for db."""
from models import db 
from app import app

# create table
db.drop_all()
db.create_all()