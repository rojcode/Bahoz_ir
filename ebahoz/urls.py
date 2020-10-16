from django.urls import path

from . import views
from .views import courses_list,course_detail

app_name = "ebahoz"
urlpatterns = [
    path('',courses_list,name="home"),
    path('<slug>/<title>/course/',course_detail,name="detail"),
]


