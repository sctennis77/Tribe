# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from models import Shirt, Destination
from django.template import RequestContext
import json
def home(request):
	data_dict = {}
	shirt_list = get_shirts()
	data_dict['shirt_list'] = shirt_list


	return render_to_response('shirtview.html',data_dict,RequestContext(request))


def get_shirts():
	shirt_query_result = Shirt.objects.all()
	return shirt_query_result 


def get_shirt_info(request):
	# will get sent shirt data as JSON by form
	# as of now is a test function
	print request
	response_data = {'success':'true'}
	return HttpResponse(json.dumps(response_data), mimetype="application/json")
