from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from Users import views as user_view
from Projects import views as project_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('project/', include('Projects.urls', namespace="home"))
    # i can remove the "project/" to get into with out writing /project in url
    path('project/', include('Projects.urls', namespace='Projects')),
    path('', include('Users.urls')),
    path('search/',project_view.search),
    path('addproject/<int:id>',project_view.create_project),
    path('register/', user_view.register, name="register"),  
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
