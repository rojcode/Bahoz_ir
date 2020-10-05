from django.contrib import admin

# Register your models here.
from account_k.models import account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['username','phone','ip_user']

    class Meta:
        model = account


admin.site.register(account,AccountAdmin)
