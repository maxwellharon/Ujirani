from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from hoodwatch.models import Hoodwatch, HoodwatchMember

# Create your views here.


class CreateHoodwatch(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'location')
    model = Hoodwatch


class SingleHoodwatch(generic.DetailView):
    model = Hoodwatch


class ListHoodwatchs(generic.ListView):
    model = Hoodwatch

'''
    This view function will enable new users join a given hoodwatch
'''
class JoinHoodwatch(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('hoodwatch:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        hoodwatch = get_object_or_404(Hoodwatch, slug=self.kwargs.get('slug'))

        try:
            HoodwatchMember.objects.create(user=self.request.user, hoodwatch=hoodwatch)
        except IntegrityError:
            messages.warning(self.request, ' You are already a member!')
        else:
            messages.success(self.request, 'Welcome to the Ujirani Community :-)')

        return super().get(request, *args, **kwargs)
        # https://rhettinger.wordpress.com/2011/05/26/super-considered-super/

'''
    This view function will eneble users to exit a hoodwatch
'''
class LeaveHoodwatch(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('hoodwatch:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            membership = HoodwatchMember.objects.filter(user=self.request.user, hoodwatch__slug=self.kwargs.get('slug')).get()
        except HoodwatchMember.DoesNotExist:
            messages.warning(self.request, ' You are already a resident here :-)')
        else:
            membership.delete()
            messages.success(self.request, 'You are part of Ujirani :-)')

        return super().get(request, *args, **kwargs)
