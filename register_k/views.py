from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from register_k.forms import register_form
from ipaddr import client_ip
from account_k.models import account

User = get_user_model()


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    rf = register_form(request.POST or None,request.FILES or None)



    context = {
        'form': rf,
        }

    if rf.is_valid():
        username = rf.cleaned_data.get('username')
        email = rf.cleaned_data.get('email')
        phone = rf.cleaned_data.get('phone')
        password = rf.cleaned_data.get('password')
        image = rf.cleaned_data.get('image_profile')
        ip = client_ip(request)

        # user = User.(username=username,email=email,password=password)
        user = User.objects.create_user(username=username,email=email,password=password)
        user_inf = account(user=user,username=username,phone=phone,ip_user=ip,image=image)
        user_inf.save(request)

        context['form'] = register_form()
        return redirect('/check_register')

    return render(request,"register/register.html",context)
