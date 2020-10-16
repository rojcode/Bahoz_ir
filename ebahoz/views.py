from django.db.models import Q
from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.views.generic import ListView

from ebahoz.models import Course


def courses_list(request):
    courses = Course.free_courses.all()
    return render(request,'ebahoz/home.html',{'courses': courses})


def course_detail(request,slug,title):
    course = get_object_or_404(Course,slug=slug,title=title,status="Free")
    downloads_link = course.downloads.all()
    return render(request,'ebahoz/detail.html',{'course': course,'downloads': downloads_link})
