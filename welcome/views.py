import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
from . import forms

# Create your views here.

def index(request):
    # hostname = os.getenv('HOSTNAME', 'unknown')
    # PageView.objects.create(hostname=hostname)
    if request.method == 'GET':
        form = forms.SignInfoForm()
    else:
        form = forms.SignInfoForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'welcome/index.html', {
        'form': form,
        'database': database.info(),
    })

def health(request):
    return HttpResponse(PageView.objects.count())
