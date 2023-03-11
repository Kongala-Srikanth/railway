from django.contrib import admin
from trainApp.models import UserDetails

# Register your models here.
class table_form(admin.ModelAdmin):
    list_display = ['From_location','To_location','Mobile','Date','Gender']

admin.site.register(UserDetails,table_form)