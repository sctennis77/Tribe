from django.contrib import admin
from shirtshop.shirts.models import Shirt, Destination
from django.db import models



class Shirt(models.Model):
	class Admin:
		list_display = ("pattern","price","serial")

class Destination(models.Model):
	class Admin:
		last_displace = ("first_name","last_name","address")
admin.site.register(Shirt)