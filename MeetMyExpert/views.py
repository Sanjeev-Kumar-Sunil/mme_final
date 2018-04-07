from django.views.generic import TemplateView

from MeetMyExpert.forms import ContactForm
from django.shortcuts import render


class WelcomePage(TemplateView):
    template_name = 'log_in_successful.html'


class HomePage(TemplateView):
    template_name = 'index.html'










