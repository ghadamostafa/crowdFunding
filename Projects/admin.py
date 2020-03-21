from django.contrib import admin
from .models import Categories,Projects,Comments,Featured_projects

admin.site.register(Categories)
admin.site.register(Projects)
admin.site.register(Comments)
admin.site.register(Featured_projects)

