# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import FormView
from form.forms import ExampleForm

# Create your views here.


class ExampleFormView(FormView):
    form_class = ExampleForm
    template_name = 'form.html'