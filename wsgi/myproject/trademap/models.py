from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # for extended User model usage, please refer to:
    # http://stackoverflow.com/questions/6085025/django-user-profile

    user = models.OneToOneField(User, related_name='profile')
    phone = models.CharField(max_length=12)
    home_lat = models.DecimalField(max_digits=19, decimal_places=10, null=True)
    home_lng = models.DecimalField(max_digits=19, decimal_places=10, null=True)
    dob = models.DateTimeField("Date of Birth")

    def __str__(self):
        return self.user.first_name
