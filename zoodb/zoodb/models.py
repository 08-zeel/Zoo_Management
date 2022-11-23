# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class zoo(models.Model):
    zoo_id = models.IntegerField(primary_key=True)
    zoo_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    hospital_id = models.IntegerField()
    ticket_id = models.IntegerField()
    class Meta:
        db_table ="zoo"

class ticket (models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    ticket_price = models.IntegerField()
    class Meta:
        db_table ="ticket"

class animal (models.Model):
    animal_id = models.IntegerField(primary_key=True)
    animal_name = models.CharField(max_length=100)
    count = models.IntegerField()
    extinction_id = models.IntegerField()
    health_id = models.IntegerField()
    class Meta:
        db_table ="animal"


