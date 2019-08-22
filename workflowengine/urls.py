"""workflowengine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .apiviews.FieldAPIView import *
from .apiviews.FormFieldAPIView import *
from .apiviews.UserFlowAPIView import *
from .apiviews.FormDataAPIView import *
from workflowengine.riverapiviews.StateAPIView import *
from workflowengine.riverapiviews.TransitionApprovalAPIView import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api-auth/', include('rest_framework.urls')),
    path('modifyField/<pk>', FieldRUD.as_view()),
    path('createField/', FieldCreate.as_view()),
    path('viewFields/', FieldList.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('getFormFields/', FormFieldList.as_view()),
    path('getPendingFlows/', getPendingFlows.as_view()),
    path('getCompletedFlows/', getCompletedFlows.as_view()),
    path('getFieldData/<int:flow_id>', FormDataList.as_view()),
    path('getFieldData/<int:flow_id>/<int:stage>', FormDataListByStage.as_view()),
    
    path('getStates/', StateList.as_view()),
    
    path('getFlowHistory/<int:flow_id>', getFlowHistory.as_view()),
    path('getTransition/<int:flow_id>', availableTransitionApprovals.as_view()),


    
    
    
    
]
