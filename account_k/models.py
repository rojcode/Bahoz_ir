import os
import random
import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext


def upload_image_path(instance,filename):
    new_name = random.randint(1,25513521)
    name,ext = get_filename_ext(filename)
    # final_name = f"{new_name}{ext}"
    final_name = f"{instance.username}{ext}"
    return f"p/{new_name}/{final_name}"


class account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,verbose_name="کاربر")
    username = models.CharField(max_length=120,verbose_name="نام کاربری")
    phone = models.CharField(max_length=120,blank=True,verbose_name="شمارە تلفن")
    ip_user = models.CharField(max_length=120,blank=True,verbose_name="Ip کاربر")
    image = models.ImageField(upload_to=upload_image_path,verbose_name="عکس پروفایل")

    class Meta:
        verbose_name = 'اطلاعات بیشتر کاربر'
        verbose_name_plural = 'اطلاعات بیشتر کاربران'

    def __str__(self):
        return self.username
