from django.db import models
from django.contrib.auth.models import User


class wrong_word(models.Model):
    farsi = models.CharField(max_length=120,verbose_name="فارسی")
    kurdish = models.CharField(max_length=120,verbose_name="کردی")
    why_wrong = models.TextField(verbose_name="علت اشتباە بودی")
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    answer = models.TextField(blank=True,default='بدون جواب',verbose_name="جواب ما")

    class Meta:
        verbose_name = 'کلمه اشتباە'
        verbose_name_plural = 'کلمات اشتباە'

    def __str__(self):
        return self.farsi
