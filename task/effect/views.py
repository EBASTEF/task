# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os.path import isfile
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from effect.tasks import save_to_pdf

# Create your views here.


def effect_view(request):
    if request.method != 'POST' and not isfile('static/pdfs/example_file1.pdf'):
        return HttpResponseRedirect('/')
    
    if request.method == 'POST':
        first = request.POST['first_name']
        last = request.POST['last_name']
        date = request.POST['date_of_birth']
        email = request.POST['email']
        number = request.POST['favourite_number']
        continent = request.POST['your_continent']
        save_to_pdf.delay(first, last, date, email, number, continent)
    templ = loader.get_template('effect.html')

    return HttpResponse(templ.render({}, request))