from peewee import *

db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port='5432')

class BaseModel(Model):
	class Meta:
		database = db


class Contact(BaseModel):
	fname = CharField()
	lname = CharField()
	email = CharField()
	phone = IntegerField()

db.connect()
db.create_tables([Contact])