from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from . import models
from . import forms
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


class BusinessList(SelectRelatedMixin, generic.ListView):
    model = models.Business
    select_related = ('user', 'hoodwatch')

class UserBusinesses(generic.ListView):
    model = models.Business
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.business_user = User.objects.prefetch_related('businesses').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.business_user.businesses.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['business_user'] = self.business_user
        return context
