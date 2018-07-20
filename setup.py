from model import db, SavedDonation

db.connect()
db.create_tables([SavedDonation])