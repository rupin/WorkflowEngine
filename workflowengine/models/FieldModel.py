from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from river.models.fields.state import StateField
from river.models import State


class Field(models.Model):	
	field_description=models.CharField(max_length=200, default='')
	field_question=models.CharField(max_length=300, default='')
	


	FIELD_DISPLAY = (
						('NONE', 'NONE'),
						("FULLDATE", "FULLDATE"),
						("DATE", "DATE"),
						("MONTH", "MONTH"),
						("YEAR", "YEAR"),
						('FULLDATE_TEXT_MONTH','FULLDATE_TEXT_MONTH'),
						('CHECK_BOX','CHECK_BOX'),
						('MULTICHOICE','MULTICHOICE')
					)
	
	field_display = models.CharField(max_length=20,choices=FIELD_DISPLAY,default="NONE")	

	FIELD_TYPE = (
						('TEXT', 'TEXT'),
						("LONG_TEXT", "LONG_TEXT"),
						("DATE", "DATE"),						
						('FULLDATE_TEXT_MONTH','FULLDATE_TEXT_MONTH'),
						('CHECK_BOX','CHECK_BOX'),
						('MULTICHOICE','MULTICHOICE')
				)

	field_type=models.CharField(max_length=20,choices=FIELD_TYPE,default="TEXT")	
	multichoice_options=models.CharField(max_length=200,default='', null=True)

	def __str__(self):
		return self.field_description
	class Meta:
		
		app_label="workflowengine"
