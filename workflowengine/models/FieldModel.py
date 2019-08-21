from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from river.models.fields.state import StateField
from river.models import State


class Field(models.Model):	
	description=models.CharField(max_length=200, default='')
	question=models.CharField(max_length=300, default='', null=True,blank=True)
	label=models.CharField(max_length=200, default='')	

	FIELD_TYPE = (
						('TEXT', 'TEXT'),
						("LONG_TEXT", "LONG_TEXT"),
						("DATE", "DATE"),
						("DATETIME", "DATETIME"),						
						('CHECK_BOX','CHECK_BOX'),
						('MULTICHOICE','MULTICHOICE'),
						('RADIO', 'RADIO'),
						('FILE', 'FILE')
				)

	field_type=models.CharField(max_length=20,choices=FIELD_TYPE,default="TEXT")	
	multichoice_options=models.CharField(max_length=200,default='', null=True, blank=True)

	def __str__(self):
		return self.description


	class Meta:		
		app_label="workflowengine"
