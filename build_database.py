import os
from config import db
from models import Person

# Data to initialize database with
PEOPLE = [
    {"fname": "Zach", "lname": "Boukli"},
    {"fname": "Simoni", "lname": "Fobi"},
    {"fname": "Brendan", "lname": "Kelley"},
    {"fname": "Nick", "lname": "Kolowich"},
    {"fname": "Michael", "lname": "McFall"},
    {"fname": "Matthew", "lname": "Miller"},
    {"fname": "Sulaimon", "lname": "Oyeleye"},
    {"fname": "Prasann", "lname": "Ranade"},
    {"fname": "Rock", "lname": "Shi"},
    {"fname": "Mark", "lname": "Subra"},
    {"fname": "Cameron", "lname": "Walker"},
]

# Delete database file if it exists currently
if os.path.exists("people.db"):
    os.remove("people.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person.get("lname"), fname=person.get("fname"))
    db.session.add(p)

db.session.commit()
