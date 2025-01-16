# defines all Django models
from datetime import datetime, timezone
from django.db import models

from app.django_orm import utils

utils.ensure_django()

def get_current_datetime():
    return datetime.now(timezone.utc)

class MALANRawResource(models.Model):
    location = models.TextField(null=True, blank=True)
    last_updated = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    aid_type = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    animals = models.TextField(null=True, blank=True)
    volunteers_needs = models.TextField(null=True, blank=True)
    accepting = models.TextField(null=True, blank=True)
    providing = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    source = models.TextField(null=True, blank=True)
    closed = models.BooleanField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)


# class need_help(models.Model):
#     id = models.BigIntegerField(primary_key=True)           #primary key of table
#     fk_tableName = models.CharField(max_length=64)          #source table name
#     fk_id = models.BigIntegerField()                        #primary key of source table
#     original_source = models.CharField(max_length=64)       #original source aid came from
#     aid_type = models.CharField(max_length=64)              #aid classification (eg shelter, meals, info, etc.)
#     aid_name = models.CharField(max_length=128)             #short name of available resource
#     aid_description = models.CharField(max_length=512)      #long description of available resource
#     aid_address = models.CharField(max_length=256)          #address of aid available
#     aid_neighborhood = models.CharField(max_length=64)      #neighborhood of aid available
#     aid_zipcode = models.CharField(max_length=10)           #zipcode of aid available; 5-digit + 4
#     aid_county = models.CharField(max_length=32)            #county of aid available
#     hours_availability = models.CharField(max_length=64)    #hours of operations and/or availability
#     aid_contact_phone = models.CharField(max_length=16)     #contact number for aid
#     aid_contact_name = models.CharField(max_length=64)      #contact name for aid
#     aid_notes = models.CharField                            #additional notes/comments

# class give_help(models.Model):
#     id = models.BigIntegerField(primary_key=True)               #primary key of table
#     fk_tableName = models.CharField(max_length=64)              #source table name
#     fk_id = models.BigIntegerField()                            #primary key of source table
#     original_source = models.CharField(max_length=64)           #original source resource came from
#     resource_type = models.CharField(max_length=64)             #resource classification (eg time, money, transportation, etc.)
#     resource_name = models.CharField(max_length=128)            #short name of available resource
#     resource_description = models.CharField(max_length=512)     #long description of available resource
#     resource_address = models.CharField(max_length=256)         #address of resource
#     resource_neighborhood = models.CharField(max_length=64)     #neighborhood of resource
#     resource_zipcode = models.CharField(max_length=10)          #zipcode of resource; 5-digit + 4
#     resource_county = models.CharField(max_length=32)           #county of resource
#     resource_service_area = models.CharField(max_length=64)     #the area the resource is available to travel
#     hours_availability = models.CharField(max_length=64)        #hours of operations and/or availability
#     resource_contact_phone = models.CharField(max_length=16)    #contact numbrer for resource
#     resource_contact_name = models.CharField(max_length=64)     #contact name for resource
#     resource_notes = models.CharField                           #additional notes/comments
