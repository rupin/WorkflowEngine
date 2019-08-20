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
from workflowengine.models import UserRoleModel
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel.CustomUser		


admin.site.register(CustomUserModel.CustomUser, CustomUserAdmin)
admin.site.register(FieldModel.Field)
admin.site.register(FlowModel.Flow)
admin.site.register(FormModel.Form)
admin.site.register(FormFieldModel.FormField)
admin.site.register(UserRoleModel.UserRole)


