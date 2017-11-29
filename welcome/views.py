# -*- coding: utf-8 -*-
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
    comment = ''
    if request.method == 'GET':
        form = forms.SignInfoForm()
    else:
        form = forms.SignInfoForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.SignInfoForm()
            comment = '操作成功'
    return render(request, 'welcome/index.html', {
        'form': form,
        'database': database.info(),
        'comment':comment
    })



def health(request):
    return HttpResponse(PageView.objects.count())
