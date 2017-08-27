from django.db import models
from django.contrib.auth.models import User


class Concert(models.Model):
    band = models.CharField(required=True, max_length=128, blank=False, default='')
    date = models.DateField(required=True)
    city = models.CharField(required=True, max_length=128, blank=False, default='')
    venue = models.CharField(required=False, max_length=128, blank=False, default='')
    want_level = models.IntegerField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)