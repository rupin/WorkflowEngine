from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    

class CaseUserAdmin(UserAdmin):    
	model = Flow
	

class DocumentUserAdmin(UserAdmin):    
	model = Document
	


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Flow)
admin.site.register(Document)

