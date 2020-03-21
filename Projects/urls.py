from django.urls import path
from . import views 

urlpatterns = [
    path('<int:Id>', views.project),
]