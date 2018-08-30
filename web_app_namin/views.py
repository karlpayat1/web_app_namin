from pyramid.view import view_config
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
	if 'switch' in request.params:
		GPIO.output(10, request.params['switch'] == "ON")
	if 'blink' in request.params:
		os.system("python3 /home/pi/Desktop/blink.py")
	return {'project': 'web-app-namin'}

def app_users(request):
	finame=str(request.POST.get('firstname'))
	laname=str(request.POST.get('lastname'))
	dcrption=str(request.POST.get('description'))
	uname=str(request.POST.get('username'))
	pnumber=str(request.POST.get('phonenumber'))
	if AppUsers.objects(username=uname).first():
		return{"error": "USERNAME ALREADY EXISTS"}
	x=AppUsers(firstname=finame,lastname=laname,description=dcrption,username=uname,phonenumber=pnumber)
	x.save()
	return{"response": "DATA ADDED"}
