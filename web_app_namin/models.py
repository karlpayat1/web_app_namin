from mongoengine import *
from datetime import datetime
import hashlib
#connect to a mongodb database
connect('database_namin')

'''hashes a string using md5 hashing algorithm
	returns a 32 character-length hashed string'''
def hash_mo_to(raw_string):
	hasher=hashlib.md5()
	hasher.update(raw_string.encode('ascii'))
	return str(hasher.hexdigest())

#default admin credentials for the system
class Admin(DynamicDocument):
	username=StringField(default='admin')
	password=StringField(default=hash_mo_to('admin'))
#schema for mobile application users set by the admin...
class AppUsers(DynamicDocument):
	firstname=StringField()
	lastname=StringField()
	username=StringField()
	password=StringField(default=hash_mo_to("1234"))
