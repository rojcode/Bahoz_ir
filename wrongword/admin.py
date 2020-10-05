from django.contrib import admin

from wrongword.models import wrong_word


class WordAdmin(admin.ModelAdmin):
    list_display = ['farsi','kurdish','why_wrong','user','answer']

    class Meta:
        model = wrong_word


admin.site.register(wrong_word,WordAdmin)
