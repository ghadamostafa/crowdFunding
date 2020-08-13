from django.contrib import admin
from .models import Categories,Projects,Comments,Rates,Pictures

admin.site.register(Categories)
admin.site.register(Projects)
admin.site.register(Comments)


#not necessary
admin.site.register(Rates)
admin.site.register(Pictures)
