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
	home = input("Would you like to add a contact or view, update, or delete an existing one? Type 'a', 'v', 'u', or 'd': ")
	if home == 'a':
		fname = input("Enter first name: ")
		lname = input("Enter last name: ")
		email = input("Enter email: ")
		print("Contact added!")
		new_contact = Contact(fname=fname, lname=lname, email=email)
		new_contact.save()
		on_load()
	elif home == 'v':
		view = input("View all or search? Type 'va' or 's': ")
		if view == 'va':
			view_contacts = Contact.select()
			for c in view_contacts:
				print(c.fname, c.lname, c.email)
			on_load()
		elif view == 's':
			search_name = input("Search by first name: ")
			search_contacts = Contact.select()
			for c in search_contacts:
				if search_name == c.fname:
					print(c.fname, c.lname, c.email)
					on_load()
				# else:
				# 	print("No contacts by that name.")
				# 	on_load()
	


	elif home == 'd':
		seek_destroy = input("Search by first name for the contact you want to delete: ")
		delete_contacts = Contact.select()
		for c in delete_contacts:
			if seek_destroy == c.fname:
				affirm = input("Are you sure you want to utterly DESTROY this person? y/n: ")
				if affirm == 'y':
					goodbye = Contact.get(Contact.fname == seek_destroy)
					goodbye.delete_instance()
					on_load()
				elif affirm == 'n':
					print("Oh, ok. That was close.")
					on_load()








on_load()