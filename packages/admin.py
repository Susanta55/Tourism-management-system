from django.contrib import admin
from packages.models import package

# Register your models here.


class PackAdmin(admin.ModelAdmin):

    
    list_display = ('id', 'destination','location','price','duration','is_featured')
    list_display_links= ('id','destination')
    search_fields = ('destination','location')



admin.site.register(package, PackAdmin)