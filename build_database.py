import os
from config import db
from models import Person

# Data to initialize database with
PEOPLE = [
    {"first_name": "Zach", "last_name": "Boukli"},
    {"first_name": "Simoni", "last_name": "Fobi"},
    {"first_name": "Brendan", "last_name": "Kelley"},
    {"first_name": "Nick", "last_name": "Kolowich"},
    {"first_name": "Michael", "last_name": "McFall"},
    {"first_name": "Matthew", "last_name": "Miller"},
    {"first_name": "Sulaimon", "last_name": "Oyeleye"},
    {"first_name": "Prasann", "last_name": "Ranade"},
    {"first_name": "Rock", "last_name": "Shi"},
    {"first_name": "Mark", "last_name": "Subra"},
    {"first_name": "Cameron", "last_name": "Walker"},
]

# Delete database file if it exists currently
if os.path.exists("people.db"):
    os.remove("people.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(last_name=person.get("last_name"), first_name=person.get("first_name"))
    db.session.add(p)

db.session.commit()
