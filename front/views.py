import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


logger = logging.getLogger(__name__)

class IndexView(TemplateView):
    template_name = 'front/index.html'
