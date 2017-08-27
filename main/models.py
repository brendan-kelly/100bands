from django.db import models
from django.contrib.auth.models import User


class Concert(models.Model):
    band = models.CharField(max_length=128, blank=False, default='')
    date = models.DateField(blank=False)
    city = models.CharField(max_length=128, blank=False, default='')
    venue = models.CharField(max_length=128, blank=True, default='')
    want_level = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)