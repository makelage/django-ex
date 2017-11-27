#coding:utf-8
import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
from . import forms
import traceback

# Create your views here.

def index(request):
    # hostname = os.getenv('HOSTNAME', 'unknown')
    # PageView.objects.create(hostname=hostname)
    path = os.path.abspath(__file__)
    path = os.path.join(os.path.dirname(path),'..', 'exp.log')
    of = file(path,'a')
    try:
        if request.method == 'GET':
            form = forms.SignInfoForm()
        else:
            form = forms.SignInfoForm(request.POST)
            if form.is_valid():
                form.save()
        of.write(form.as_p().encode('utf8'))
        return render(request, 'welcome/index.html', {
            'form': form,
            'database': database.info(),
        })
    except:
        traceback.print_exc(None, of)
        raise
    finally:
        of.close()


def health(request):
    return HttpResponse(PageView.objects.count())
