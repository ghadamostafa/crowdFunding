from django.conf.urls import url
from . import views

app_name = "Projects"


urlpatterns = [
    url(r'^(?P<id>\d+)$', views.project_details, name="project_details"),
    url(r'^(?P<id>\d+)/edit$', views.edit_project, name="edit_project"),
    url(r'^(?P<id>\d+)/donate$', views.donate, name="donate"),
    url('save', views.save, name='save')
]
