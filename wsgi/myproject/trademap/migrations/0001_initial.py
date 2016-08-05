# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('phone', models.CharField(max_length=12)),
                ('home_lat', models.DecimalField(null=True, max_digits=19, decimal_places=10)),
                ('home_lng', models.DecimalField(null=True, max_digits=19, decimal_places=10)),
                ('dob', models.DateTimeField(verbose_name='Date of Birth')),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
