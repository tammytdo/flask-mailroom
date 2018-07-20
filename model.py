import os

from peewee import Model, CharField, IntegerField

db = connect(os.environ.get('Database_URL', 'sqlite:///my_database.db'))

class SavedDonation(Model):
    donor_value = CharField()
    donation_value = IntegerField()

    class Meta:
        database = db