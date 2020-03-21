from django.contrib import admin
from .models import Categories,Projects,Comments,Featured_projects,Rates,Pictures

admin.site.register(Categories)
admin.site.register(Projects)
admin.site.register(Comments)
admin.site.register(Featured_projects)
#not necessary
admin.site.register(Rates)
admin.site.register(Pictures)
