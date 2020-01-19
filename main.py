from peewee import *

db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port='5432')

class BaseModel(Model):
	class Meta:
		database = db

class Contact(BaseModel):
	fname = CharField(null = False)
	lname = CharField(null = False)
	email = CharField(null = False)
	phone = CharField(null = False)

db.connect()
db.drop_tables([Contact])
db.create_tables([Contact])

new_contact = None

def on_load():
	home = input("Would you like to add a contact or view, update, or delete an existing one? Type 'a', 'v', 'u', or 'd': ")
	if home == 'a':
		fname = input("Enter first name: ")
		if fname == 'x':
			on_load()
		lname = input("Enter last name: ")
		if lname == 'x':
			on_load()
		email = input("Enter email: ")
		if email == 'x':
			on_load()
		phone = input("Enter phone number: ")
		if phone == 'x':
			on_load()

		# format_phone = []
		# for char in phone:
		# 	format_phone.append(char)
		# area = ''.join(str(format_phone[0:3]))
		new_phone = '(' + phone[0:3] + ') ' + phone[3:6] + '-' + phone[6:]
		# new_phone = f"({area}) {format_phone[3:]}"
		# new_phone = ''.join(f"({format_phone[0:3]}) {format_phone[3:6]}-{format_phone[6:]}")

		print("Contact added!")
		new_contact = Contact(fname=fname, lname=lname, email=email, phone=new_phone)
		new_contact.save()
		on_load()
	elif home == 'v':
		view = input("View all or search? Type 'va' or 's': ")
		if view == 'x':
			on_load()
		if view == 'va':
			view_contacts = Contact.select()
			for c in view_contacts:
				print(f"{c.fname} | {c.lname} | {c.email} | {c.phone}")
			on_load()
		elif view == 's':
			search_name = input("Search by first name: ")
			search_contacts = Contact.select()
			for c in search_contacts:
				if search_name == c.fname:
					print(f"{c.fname} | {c.lname} | {c.email} | {c.phone}")
					on_load()
			else:
				print("Contact does not exist.")
			on_load()
	elif home == 'u':
		update_contact = input("Search by first name for the contact you want to update: ")
		if update_contact == 'x':
			on_load()
		search_update = Contact.select()
		for c in search_update:
			if update_contact == c.fname:
				new_update = Contact.get(Contact.fname == update_contact)
				update_field = input("Which field do you want to update? fname/lname/email: ")
				if update_field == 'fname':
					new_update.fname = input("New first name: ")
					new_update.save()
				elif update_field == 'lname':
					new_update.lname = input("New last name: ")
					new_update.save()
				elif update_field == 'email':
					new_update.email = input("New email: ")
					new_update.save()
				elif update_field == 'phone':
					new_update.phone = input("New phone number: ")
					new_update.save()
			else:
				print("Contact does not exist.")
			on_load()

	elif home == 'd':
		seek_destroy = input("Search by first name for the contact you want to delete: ")
		if seek_destroy == 'x':
			on_load()
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
				else:
					print("Deletion aborted.")
				on_load()
			else:
				print("Contact does not exist.")
			on_load()

	else:
		print("Please type one of the approved commands.")
		on_load()


on_load()