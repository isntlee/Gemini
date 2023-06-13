from django.urls import path
from . import views

app_name = 'agents'

urlpatterns = [
    path("", views.AgentListView.as_view(), name="agent_list"), 
    path("create/", views.AgentCreateView.as_view(), name="agent_create")
]
