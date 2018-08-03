from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
'''
This view function is responsible for when the user logs in and sees the homepage
'''

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
