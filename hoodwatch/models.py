from django.db import models
from django.utils.text import slugify
from django import template
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse


# Create your models here.
User = get_user_model()
reigster = template.Library


class Hoodwatch(models.Model):
    name = models.CharField(max_length=140, unique=True)
    slug = models.SlugField(allow_unicode=True,  unique=True)
    location = models.CharField(max_length=140, blank=True, default='')
    occupants = models.ManyToManyField(User, through='HoodwatchMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('hoodwatch:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class HoodwatchMember(models.Model):
    hoodwatch = models.ForeignKey(Hoodwatch, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_hoodwatchs')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('hoodwatch', 'user')
