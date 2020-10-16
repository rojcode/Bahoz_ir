

from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Free_Course_Manager(models.Manager):
    def get_queryset(self):
        return super(Free_Course_Manager,self).get_queryset().filter(status='Free')


class Price_Course_Manager(models.Manager):
    def get_queryset(self):
        return super(Price_Course_Manager,self).get_queryset().filter(status='Price')


class Download(models.Model):
    title = models.CharField(max_length=250,verbose_name="پارت")
    url_download = models.URLField(verbose_name="لینک دانلود")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "لینک دانلود"
        verbose_name_plural = "لینک های دانلود"

    def __str__(self):
        return self.title


class Course(models.Model):
    STATUS_CHOISE = (
        ('Free','free'),
        ('PRICE','price'),)

    title = models.CharField(max_length=250,verbose_name="نام درس")
    slug = models.SlugField(max_length=250,unique_for_date='created',verbose_name="مقدار نمایشی در url")
    des = models.TextField(verbose_name="توضیح دربارە درس")
    price = models.CharField(max_length=250,verbose_name="قیمت")
    GB = models.CharField(max_length=250,null=True,verbose_name="حجم درس")
    downloads = models.ManyToManyField(Download,related_name='downloads',blank=True,verbose_name="لینک های دانلود")
    poster = models.ImageField(upload_to='ebahoz/poster/',blank=True,verbose_name="آپلود پوستر")
    status = models.CharField(max_length=50,choices=STATUS_CHOISE,default='Free',verbose_name="نوع آموزش")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    objects = models.Manager
    free_courses = Free_Course_Manager()
    price_courses = Price_Course_Manager()

    class Meta:
        ordering = ('-created',)
        verbose_name = "آموزش"
        verbose_name_plural = "آموزش ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ebahoz:detail',args=[self.slug,self.title])
