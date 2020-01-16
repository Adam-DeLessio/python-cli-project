from peewee import *

db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port='5432')

class BaseModel(Model):
	class Meta:
		database = db


class Contact(BaseModel):
	fname = CharField(null = False)
	lname = CharField(null = False)
	email = CharField(null = False)
	# phone = IntegerField()

db.connect()
# db.drop_tables([Contact])
db.create_tables([Contact])

# adam = Contact(fname='Adam', lname='DeLessio', email='adamdelessio@gmail.com')
# adam.save()

def on_load():
	home = input("Would you like to add a contact or view existing ones? Type 'add' or 'view': ")
	if home == 'add':
		fname = input("Enter first name: ")
		lname = input("Enter last name: ")
		email = input("Enter email: ")
		new_contact = Contact(fname=fname, lname=lname, email=email)
		new_contact.save()
		on_load()
	elif home == 'view':
		contact = Contact.select()
		for c in contact:
			print(c.fname, c.lname, c.email)








on_load()