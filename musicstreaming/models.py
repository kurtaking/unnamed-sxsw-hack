from __future__ import unicode_literals

from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=512)

    def __unicode__(self):
        return str(self.user_id)


class Music(models.Model):
    music_id = models.AutoField(primary_key=True)
    music_name = models.CharField(max_length=512, default='')
    users = models.ManyToManyField(User, through='Forkship')

    def __unicode__(self):
        return str(self.music_id)


class Track(models.Model):
    track_id = models.AutoField(primary_key=True)
    pathname = models.CharField(max_length=512)
    music = models.ForeignKey(Music)

    def __unicode__(self):
        return self.pathname


class Forkship(models.Model):
    user = models.ForeignKey(User)
    music = models.ForeignKey(Music)
