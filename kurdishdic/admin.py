import csv

from django.contrib import admin
from django.http import HttpResponse

from kurdishdic.models import kurdishdic


class KurdishDicAdmin(admin.ModelAdmin):
    list_display = ['persian','sorani']

    search_fields = ('persian','sorani','simple_sorani',)

    actions = ["export_as_csv"]

    def export_as_csv(self,request,queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj,field) for field in field_names])

        return response

    export_as_csv.short_description = "گرفتن نسخه پشتیبانی از کلمات"


class Meta:
    model = kurdishdic


admin.site.register(kurdishdic,KurdishDicAdmin)


