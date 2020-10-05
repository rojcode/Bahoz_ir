from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from ipaddr import client_ip

from account_k.models import account
from update_k_account.forms import update_form_account


def update_page(request,userid=None,*args,**kwargs):
    if not request.user.is_authenticated:
        return redirect('/')

    uf = update_form_account(request.POST or None,request.FILES or None)

    context = {
        'form': uf,
        }

    if uf.is_valid():
        username = uf.cleaned_data.get('username')
        email = uf.cleaned_data.get('email')
        phone = uf.cleaned_data.get('phone')
        password = uf.cleaned_data.get('password')
        image_up = uf.cleaned_data.get('image_profile')
        ip = client_ip(request)

        user = User.objects.get(pk=userid)
        user.pk = userid
        user.username = username
        user.email = email
        user.set_password(password)
        user.save()

        new_account = account.objects.get(user=request.user)
        new_account.username = username
        new_account.phone = phone
        new_account.ip_user = ip
        new_account.image = image_up
        new_account.save()
        context['form'] = update_form_account()
        return redirect('/login')

    return render(request,"Update_account/update.html",context)
