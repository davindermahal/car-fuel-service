from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html', {})


def is_authorized_or_sign_in(request):
    if request.user.is_authorized is not True:
        return HttpResponseRedirect('/accounts/signin/')
