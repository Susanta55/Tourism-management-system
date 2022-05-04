from django.contrib import admin
from packages.models import package, booking_tour

# Register your models here.

class bookAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname','lastname','trip_name','mobile','country','is_paid')
    list_display_links= ('id','firstname')
    list_editable = ('is_paid',)
admin.site.register(booking_tour, bookAdmin)

class PackAdmin(admin.ModelAdmin):

    
    list_display = ('destination','location','price','duration','is_featured')
    list_display_links= ('destination','location')
    search_fields = ('location','destination')
    list_filter = ('location','price')
    list_editable = ('is_featured',)



admin.site.register(package, PackAdmin)



