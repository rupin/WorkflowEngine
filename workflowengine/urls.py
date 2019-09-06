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
from workflowengine.apiviews.FieldAPIView import *
from workflowengine.apiviews.FormFieldAPIView import *
from workflowengine.apiviews.UserFlowAPIView import *
from workflowengine.apiviews.FormDataAPIView import *
from workflowengine.apiviews.FlowAPIView import *
from workflowengine.apiviews.ExpertiseAPIView import *
from workflowengine.apiviews.ExpertAPIView import *
from workflowengine.riverapiviews.StateAPIView import *
from workflowengine.riverapiviews.TransitionApprovalAPIView import *
from workflowengine.apiviews.RoleAPIView import *
from workflowengine.apiviews.CustomUserAPIView import *
import uuid



urlpatterns = [
    path('admin/', admin.site.urls),   


    
    path('rest-auth/', include('rest_auth.urls')),


    #Form Data and Fields
    path('FormFieldsByStage/<int:stage>', FormFieldsByStage.as_view()),
    path('getFieldData/<uuid:flow_id>/<uuid:formfield>', FormDataView.as_view()),
    #path('getFieldDataByStage/<int:flow_id>/<int:stage>', FormDataByStage.as_view()),
    #path('RetrieveUpdateFormData/<uuid:flow_id>/<uuid:pk>', RetrieveUpdateFormData.as_view()),
    path('createOrUpdateFormData/<uuid:flow_id>', createFormData.as_view()),
    

    #Workflow States
    path('getStates/', StateList.as_view()),
    path('getInitialState/', InitialState.as_view()),
    path('getFinalStates/', FinalStates.as_view()),
    

    #Flow Actions
    path('getPendingFlows/', getPendingFlows.as_view()),
    path('getCompletedFlows/', getCompletedFlows.as_view()),
    path('getFlowHistory/<uuid:flow_id>', getFlowHistory.as_view()),
    path('getTransition/<uuid:flow_id>', availableTransitionApprovals.as_view()),
    path('approveStage/<uuid:flow_id>', approveStage.as_view()),
    path('approveStage/<uuid:flow_id>/<int:destination>', approveStage.as_view()),
    path('createFlow/', createFlow.as_view()),


    #Experts
    path('getExpertiseList/', getExpertise.as_view()),
    path('getExpertise/<uuid:user>', getUserExpertInfo.as_view()),

    
    #Roles
    path('getRoles/', RoleAPIView.as_view()),

    #profile
    path('createOrUpdatePIN/<uuid:pk>', AddUpdatePin.as_view()),
    path('validatePIN/<int:pin>', ValidatePin.as_view()),
    path('createNewUser/', UserCreateAPIView.as_view())
    
    
    
    
]
