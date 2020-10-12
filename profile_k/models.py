from django.db import models


# Create your models here.


class Profile_Bio(models.Model):
    name = models.CharField(max_length=250,verbose_name="نام")
    image = models.ImageField(upload_to='Upload/image/profiles',blank=True,verbose_name="عکس پرۆفایل")
    job = models.CharField(max_length=250,verbose_name="جایگاە")
    des = models.TextField(blank=True,verbose_name="توضیحات")
    telegram = models.URLField(default="t.me/",verbose_name="ایدی تلگرام")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "اطلاعات اعضای تیم"
        verbose_name_plural = "اطلاعات اعضای تیم"

    def __str__(self):
        return '{}--{}'.format(self.name,self.job)
