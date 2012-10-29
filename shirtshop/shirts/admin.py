from django.contrib import admin
from shirtshop.shirts.models import Shirt


#from django.db import models



#class Shirt(models.Model):
#	class Admin:
#		fields = ("serial","pattern","price","quality","description","sleeve_type","display")

admin.site.register(Shirt)


