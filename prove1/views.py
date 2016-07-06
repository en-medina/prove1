from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response 
import datetime
from django.template.loader import get_template



#Using a base template to create childs templates
def current_datetime(request):
	current_date = datetime.datetime.now()
	return render_to_response('current_date_extends.html', locals())





"""
#Using locals() functions to create the dictionary of variable that we need.
#Note that the name of the variable need to match in the view and the template
def current_datetime(request):
	current_date = datetime.datetime.now()
	return render_to_response('current_date.html', locals())
"""

"""
#using render_to_response for the process of get the template and context it
def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_date.html', {'current_date' : now})
"""


"""
def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_date.html')
	html = t.render(Context({'current_date': now}))
		#html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
"""


def hours_ahead(request, added_hours):
	added_hours = int(added_hours)
	future_date = datetime.datetime.now() + datetime.timedelta(hours=added_hours)
	return render_to_response('future_date_extends.html', locals())

"""
#Simple request and respond manage
def hours_ahead(request, offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)
"""



