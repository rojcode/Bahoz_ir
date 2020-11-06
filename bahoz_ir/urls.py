"""bahoz_ir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from bahoz_ir import settings
from update_k_account.views import update_page
from .views import SearchWord,home_page,yes_page,not_found_page,logout_view,your_voice,check_login,about_bahoz, \
    SearchSad,home_sad
from register_k.views import register_page
from login_k.views import login_page
from detailview.views import product_detail_view
from profile_k.views import profile_page,team_list

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',home_page,name='home'),
    path('words/search',SearchWord.as_view(),name='search'),
    path('register',register_page,name='register'),
    path('login',login_page,name='login'),
    path('words/<productid>',product_detail_view),
    path('profile',profile_page,name='profile'),
    path('check_register',yes_page,name='check_register'),
    path('not_found_page',not_found_page,name='not_found_page'),
    path('profile/update/<userid>',update_page),
    path("logout",logout_view),
    path("your_voice",your_voice),
    path("sl",check_login),
    path("bahoz-team/",team_list,name="bahoz_team"),
    path("about-bahoz/",about_bahoz,name="about-bahoz"),
    # delete
    path('sadd',home_sad,name='home2'),
    path('words/search/sadd',SearchSad.as_view(),name='search2'),
    ]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
