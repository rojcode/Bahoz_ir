from django.db import models


# Create your models here.

class ContactAdminModel(models.Model):
    subject = models.CharField(max_length=120,verbose_name="موضوع")
    message = models.CharField(max_length=120,verbose_name="پیغام")
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=120,verbose_name="کاربر")

    class Meta:
        verbose_name = 'ارتباط با مدیر'
        verbose_name_plural = 'ارتباط با مدیران'

    def __str__(self):
        return self.subject
