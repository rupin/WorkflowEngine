from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from workflowengine.models import CustomUserModel
from workflowengine.models import FlowModel
from workflowengine.models import FieldModel
from workflowengine.models import FormModel
from workflowengine.models import FormFieldModel
from workflowengine.models import RoleModel
from workflowengine.models import UserFlowModel
class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUserModel.CustomUser
	list_display = ["email", "username", "role", "is_staff"]
	fieldsets = UserAdmin.fieldsets + ( (None, {'fields': ('role',)}), )
	


class FlowAdmin(ImportExportModelAdmin):
	model=FlowModel.Flow
	list_display=['stage','created_at','updated_at']

class UserFlowAdmin(ImportExportModelAdmin):
	model=UserFlowModel.UserFlow
	list_display=['user','flow','created_at','updated_at']


admin.site.register(CustomUserModel.CustomUser, CustomUserAdmin)
admin.site.register(FieldModel.Field)
admin.site.register(FlowModel.Flow,FlowAdmin)
admin.site.register(FormModel.Form)
admin.site.register(FormFieldModel.FormField)
admin.site.register(RoleModel.Role)
admin.site.register(UserFlowModel.UserFlow,UserFlowAdmin)



