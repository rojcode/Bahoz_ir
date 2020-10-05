from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

from login_k.forms import Login_form


def login_page(request):
    login_form = Login_form(request.POST or None)
    if request.user.is_authenticated:
        return redirect('/')
    context = {
        'title': 'login',
        'form': login_form,
        }

    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            context['form'] = Login_form()
            return redirect('/')
        else:
            login_form.add_error('username','کاربری با مشخصات وارد شدە یافت نشد')

    return render(request,"login/login.html",context)
