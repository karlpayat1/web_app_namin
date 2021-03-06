from pyramid.view import view_config
import RPi.GPIO as GPIO
import os
from .models import *
from bson import ObjectId
from pyramid.httpexceptions import HTTPFound
from mongoengine import *

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
	if 'switch' in request.params:
		GPIO.output(10, request.params['switch'] == "ON")
	if 'blink' in request.params:
		os.system("python3 /home/pi/Desktop/blink.py")
	if 'register-now' in request.params:
		print("REGISTER")
		firstname = request.params['fname']
		lastname = request.params['lname']
		username = request.params['username']
		password = request.params['password']
		if AppUsers.objects(username=username).first():
			return{"error": "USERNAME ALREADY EXISTS"}
		x = AppUsers(firstname=firstname,lastname=lastname,username=username,password=password)
		x.save()
	return {'project': 'web-app-namin'}

def app_users(request):
	finame=str(request.POST.get('firstname'))
	laname=str(request.POST.get('lastname'))
	uname=str(request.POST.get('username'))
	if AppUsers.objects(username=uname).first():
		return{"error": "USERNAME ALREADY EXISTS"}
	x=AppUsers(firstname=finame,lastname=laname,username=uname)
	x.save()
	return{"response": "DATA ADDED"}
