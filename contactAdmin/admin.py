from django.contrib import admin


# Register your models here.
from contactAdmin.models import ContactAdminModel


class ProductAdmin(admin.ModelAdmin):
    list_display = ['subject','message','user']

    class Meta:
        model = ContactAdminModel


admin.site.register(ContactAdminModel,ProductAdmin)
