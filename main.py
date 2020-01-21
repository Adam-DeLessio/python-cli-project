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
# db.drop_tables([Contact])
# db.create_tables([Contact])

new_contact = None

print('\nYour personal contacts storage sytem.\n')
def on_load():
	home = input("Type the number for the function you wish to perform.\n1: Add\n2: View\n3: Update\n4: Delete\n:")
	if home == '1':
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

		new_phone = '(' + phone[0:3] + ') ' + phone[3:6] + '-' + phone[6:]

		print("\nContact added!\n")
		new_contact = Contact(fname=fname, lname=lname, email=email, phone=new_phone)
		new_contact.save()
		on_load()
	elif home == '2':
		view = input("\n1: View All\n2: Search\n:")
		if view == 'x':
			on_load()
		if view == '1':
			view_contacts = Contact.select()
			print('\n')
			for c in view_contacts:
				print(f"{c.fname} | {c.lname} | {c.email} | {c.phone}")
			print('\n')
			on_load()
		elif view == '2':
			search_name = input("Search by first name: ")
			search_contacts = Contact.select()
			for c in search_contacts:
				if search_name == c.fname:
					print(f"\n{c.fname} | {c.lname} | {c.email} | {c.phone}\n")
					on_load()
			else:
				print("Contact does not exist.")
			on_load()
	elif home == '3':
		update_contact = input("\nSearch by first name for the contact you want to update: ")
		if update_contact == 'x':
			on_load()

		search_update = Contact.select()
		for c in search_update:
			if update_contact == c.fname:
				new_update = Contact.get(Contact.fname == update_contact)
				update_field = input("\nWhich field do you want to update?\n1: First Name\n2: Last Name\n3: Email\n4: Phone\n")
				if update_field == '1':
					new_update.fname = input("New first name: ")
					new_update.save()
					print("\nContact updated!\n")
				elif update_field == '2':
					new_update.lname = input("New last name: ")
					new_update.save()
					print("\nContact updated!\n")
				elif update_field == '3':
					new_update.email = input("New email: ")
					new_update.save()
					print("\nContact updated!\n")
				elif update_field == '4':
					new_update.phone = input("New phone number: ")
					new_update.save()
					print("\nContact updated!\n")

		on_load()

	elif home == '4':
		seek_destroy = input("\nSearch by first name for the contact you want to delete: ")
		if seek_destroy == 'x':
			on_load()

		delete_contacts = Contact.select()
		for c in delete_contacts:
			if seek_destroy == c.fname:
				affirm = input("\nAre you sure you want to utterly DESTROY this person? y/n: ")
				print('\n')
				if affirm == 'y':
					goodbye = Contact.get(Contact.fname == seek_destroy)
					goodbye.delete_instance()
					on_load()
				elif affirm == 'n':
					print("\nOh, ok. That was close.\n")
					on_load()
				else:
					print("\nDeletion aborted.\n")
				on_load()
			on_load()

	else:
		print("\nPlease type one of the approved commands.\n")
		on_load()


on_load()