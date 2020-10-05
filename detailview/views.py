from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User

from detailview.forms import send_wrong_word
from kurdishdic.models import kurdishdic
from wrongword.models import wrong_word


# Create your views here.


def product_detail_view(request,productid=None,*args,**kwargs):
    if not request.user.is_authenticated:
        return redirect('/sl')

    word = get_object_or_404(kurdishdic,id=productid)
    form = send_wrong_word(request.POST or None)

    if form.is_valid():
        farsi = form.cleaned_data.get('farsi')
        kurdi = form.cleaned_data.get('kurdi')
        message = form.cleaned_data.get('message')
        # user = User.objects.get(username=request.user.username)
        send = wrong_word(farsi=farsi,kurdish=kurdi,why_wrong=message,user=request.user)
        send.save(request)

        return redirect('/profile')

    context = {
        "word": word,
        'form': form,
        }
    return render(request,"Detail/detail.html",context)
