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

def on_load():
	home = input("Would you like to add a contact or view existing ones? Type 'a' or 'v': ")
	if home == 'add':
		fname = input("Enter first name: ")
		lname = input("Enter last name: ")
		email = input("Enter email: ")
		new_contact = Contact(fname=fname, lname=lname, email=email)
		new_contact.save()
		on_load()
	elif home == 'view':
		view = input("View all or search? Type 'va' or 's': ")
		if view == 'va':
			contacts = Contact.select()
			for c in contacts:
				print(c.fname, c.lname, c.email)
			on_load()
		elif view == 'search':
			search_name = input("Search by first name: ")
			contacts = Contact.select()
			for c in contacts:
				if search_name == c.fname:
					print(c.fname, c.lname, c.email)
				else:
					print("No contacts by that name")
					on_load()









on_load()