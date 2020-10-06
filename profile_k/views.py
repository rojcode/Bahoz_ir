from django.shortcuts import render,redirect

from contactAdmin.forms import ContactAdminForm
from contactAdmin.models import ContactAdminModel
from profile_k.models import Profile_Bio


def profile_page(request):
    if not request.user.is_authenticated:
        return redirect('/')

    data_wrong_message = request.user.wrong_word_set.all()
    form = ContactAdminForm(request.POST or None)

    if form.is_valid():
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        new_message = ContactAdminModel(subject=subject,message=message,user=request.user.username)
        new_message.save(request)
        return redirect('/your_voice')

    context = {
        'info': data_wrong_message,
        'admin': form
        }

    return render(request,"Profile/Profile.html",context)


def team_list(request):
    teams = Profile_Bio.objects.all()
    return render(request,'team/team.html',{'teams': teams})
