# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core import serializers
from django.utils import simplejson
from models import Shirt, Destination
from django.template import RequestContext
import json
def home(request):
	shirt_list = get_shirts()





	return render_to_response('shirtview.html',{"shirts":shirt_list},RequestContext(request))


def about(request):
	return render_to_response('aboutview.html',{},RequestContext(request))



def get_shirts():
	shirt_query_result = Shirt.objects.all()
	data = serializers.serialize("json", Shirt.objects.all())

	return data


def get_shirt_info(request):
	# will get sent shirt data as JSON by form
	# as of now is a test function
	response_data = {'success':'true'}
	return HttpResponse(json.dumps(response_data), mimetype="application/json")
