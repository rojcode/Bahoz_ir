from django.db import models


class kurdishdic(models.Model):
    persian = models.CharField(max_length=120,verbose_name="فارسی")
    sorani = models.CharField(blank=True,max_length=120,verbose_name="سورانی")
    simple_sorani = models.TextField(blank=True,default='بدون مثال',null=True,verbose_name="مثال")

    class Meta:
        verbose_name = 'کلمه'
        verbose_name_plural = 'کلمات'

    def __str__(self):
        return self.persian
