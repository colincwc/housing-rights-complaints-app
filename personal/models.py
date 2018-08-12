from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.dateparse import parse_duration
from personal.choices import waiting_years, rights_themes
import datetime

"""
Broad information
"""
class Stats(models.Model):
	id = models.AutoField(primary_key=True)
	postcode = models.CharField	(null=True, max_length=10)
	date = models.DateField(null=False, default=datetime.date.today)
	theme = models.CharField(null=True, choices=rights_themes, max_length=100)
	
	class Meta:
		verbose_name_plural = "Stats"
	
	def __str__(self):
	    return "{}'s detail".format(self.id)

"""
Profile model - extra information relating to User Model
"""
class Personal(models.Model):
	id = models.AutoField(primary_key=True)
	full_name = models.CharField(null=False, max_length=255)
	date_of_birth = models.DateField(null=False, default=datetime.date.today)
	address = models.TextField(null=False)
	temp_address = models.BooleanField(null=False)
	telephone = models.CharField(null=False, max_length=255)
	num_in_household = models.IntegerField(null=False)
	num_children = models.IntegerField(null=False)
	waiting_list_time = models.CharField(null=True, choices=waiting_years, max_length=10)

	class Meta:
		verbose_name_plural = "Personal Details"

	def __str__(self):
	    return "{}'s details".format(self.full_name)
	    
"""
Complaint details
"""
# class Details(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	description
# 	condition_evidence
# 	action
# 	action_evidence
# 	response
# 	response_evidence
# 	remedy
	
	