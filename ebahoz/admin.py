from django.contrib import admin

# Register your models here.
from ebahoz.models import Course,Download


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','slug','price','poster','status','created','updated')
    list_filter = ['created']
    search_fields = ('title','slug','des','price','poster')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('',)
    date_hierarchy = 'created'
    ordering = ['created']


@admin.register(Download)
class Admin(admin.ModelAdmin):
    list_display = ('title','url_download','created','updated')
    list_filter = ['created']
    search_fields = ['title']
    date_hierarchy = 'created'
    ordering = ['created']
