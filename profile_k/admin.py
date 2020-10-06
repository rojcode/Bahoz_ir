from django.contrib import admin

# Register your models here.
from profile_k.models import Profile_Bio


@admin.register(Profile_Bio)
class Profile_Bio_Admin(admin.ModelAdmin):
    list_display = ('name','job','telegram','created','updated')
    list_filter = ['created']
    search_fields = ('name','job',)
    date_hierarchy = 'created'
    ordering = ['created']
