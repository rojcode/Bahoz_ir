from django.db.models import Q
from django.shortcuts import render,redirect
from django.views.generic import ListView

from kurdishdic.models import kurdishdic

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('/')


def home_page(request):
    count_word = kurdishdic.objects.all().count()
    context = {
        'count': count_word
        }

    return render(request,"Home/home.html",context)


def yes_page(request):
    return render(request,"Checker/Yes_account.html",{})


def your_voice(request):
    return render(request,"Checker/Your_voice.html",{})


def not_found_page(request):
    return render(request,"Checker/Not_found.html",{})


def check_login(request):
    return render(request,"Checker/login_signup.html",{})


def join_us(request):
    return render(request,"join_us/join_us.html",{})


class SearchWord(ListView):
    template_name = 'Home/home.html'
    paginate_by = 6

    def get_context_data(self,**kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['count'] = kurdishdic.objects.all().count()
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        lookup = (
                Q(persian__icontains=query) |
                Q(sorani__contains=query)
        )

        if query is not None:
            word = kurdishdic.objects.filter(lookup)
            return word
