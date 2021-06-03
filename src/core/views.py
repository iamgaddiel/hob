from django.shortcuts import render
from django.views.generic import TemplateView, CreateView


class Index(TemplateView):
    template_name = 'core/index.html'
