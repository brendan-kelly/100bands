from django.db import models
from django.contrib.auth.models import User


WANT_LEVEL = ((5, 'DEFINITELY'),
    (4, 'PROBABLY'),
    (3, 'MAYBE'),
    (2, 'NOT SURE'),
    (1, 'DONT CARE'))


class Concert(models.Model):
    band = models.CharField(max_length=128, blank=False, default='')
    date = models.DateField(blank=False)
    city = models.CharField(max_length=128, blank=False, default='')
    venue = models.CharField(max_length=128, blank=True, default='')
    want_level = models.IntegerField(choices=WANT_LEVEL, default=WANT_LEVEL[4])
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.band