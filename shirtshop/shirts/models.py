from django.db import models
import datetime

# class to keep track of where the shirt needs to be shipped
# hopefully this will be taken care of with a different library @ some point
class Destination(models.Model):
    first_name = models.CharField(default="", max_length=100)
    last_name = models.CharField(default="", max_length=100)
    street = models.CharField(default="", max_length=100)
    city = models.CharField(default="", max_length=100)
    state = models.CharField(default="", max_length=100)
    zipcode = models.CharField(default="", max_length=100)
    other = models.TextField(default="")
    date_sent = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        buf = "-" * 80
        address = "Street: %s\nCity: %s\nState: %s\nZip: %s\n"%(self.street,self.city,self.state,self.zipcode)
        name = "First: %s\nLast: %s\n"%(self.first_name,self.last_name)
        destination_string = "%s\n%s\n%s\n%s\n"%(buf,name,address,buf)
        return destination_string

# class representing each shirt object
class Shirt(models.Model):
    pattern = models.CharField(max_length=50)
    serial_number = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    size = models.CharField(max_length=3)
    quality = models.IntegerField(default=1)
    purchased = models.DateTimeField(default=datetime.datetime.now()) # time shirt was purchased
    created = models.DateTimeField(default=datetime.datetime.now()) # time pattern was released
    description = models.TextField(default="")
    sleeve_type = models.CharField(default="short", max_length=100)
    destination = models.ForeignKey(Destination)
    display = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    other = models.TextField(default="")

    def __str__(self):
        buf = "*" * 80
        shirt_string = "%s\nPattern: %s\nSerial: %d\nPrice: %f\nSize: %s\nPurchased: %s\nSent: %s\n%s\n"\
        %(buf,self.pattern,self.serial_number,self.price,self.size,self.purchased,self.sent,buf)
        return shirt_string








    