from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


WANT_LEVEL = ((5, 'DEFINITELY'),
    (4, 'PROBABLY'),
    (3, 'MAYBE'),
    (2, 'NOT SURE'),
    (1, 'DONT CARE'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO: generate unique hash or random names for share_link.
    share_link = models.CharField(max_length=256, blank=False, editable=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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