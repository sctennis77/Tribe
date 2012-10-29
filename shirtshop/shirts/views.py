# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core import serializers
from django.utils import simplejson
from models import Shirt, Destination
from django.template import RequestContext
import json
def home(request):
	shirt_json,shirt_list = get_shirts()
	# re arrange shirts will clean this later
	slider_tag_dict,thumbnail_list = build_slider_dict(shirt_list)
	shirt_dict = zip(thumbnail_list,shirt_list)
	print shirt_dict





	return render_to_response('shirtview.html',{"shirt_json":shirt_json,"shirt_list":shirt_list,'slider_tag_dict':slider_tag_dict,'thumbnail_list':thumbnail_list,"thumbnail_json":json.dumps(thumbnail_list)},RequestContext(request))


def about(request):
	return render_to_response('aboutview.html',{},RequestContext(request))


def patterns(request):
	return render_to_response('patterns.html',{},RequestContext(request))

def canvas(request):
	return render_to_response('canvas.html',{},RequestContext(request))


def get_shirts():
	shirt_query = Shirt.objects.all()
	shirt_list = list(shirt_query)
	tmp =shirt_list.pop(len(shirt_list)-1)
	shirt_list.insert(0,tmp)
	data = serializers.serialize("json", shirt_list)



	return data,shirt_list

def build_slider_dict(shirt_list):
	# populates a dictionary that will serve as a mapping to the bxslider
	# <ul> tag's class name
	slider_dict = {}
	slider_str = "slider"
	for i in range(len(shirt_list)):
		shirt_pattern = shirt_list[i].pattern
		slider_dict[shirt_pattern] = slider_str + str(i)

	thumbs = slider_dict.keys()
	tmp = thumbs.pop(len(thumbs)-1)
	thumbs.insert(0,tmp)
	print thumbs
	return slider_dict,thumbs


def get_shirt_info(request):
	# will get sent shirt data as JSON by form
	# as of now is a test function
	response_data = {'success':'true'}
	return HttpResponse(json.dumps(response_data), mimetype="application/json")
