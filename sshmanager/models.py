from django.db import models
from django.utils import timezone

class Host(models.Model):
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey('auth.User')
    host = models.CharField(max_length = 100)
    hostname = models.CharField(max_length = 100)
    user = models.CharField(max_length = 100)
    port = models.IntegerField()
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return "%s@%s:%d" % (self.user, self.hostname, self.port)

class Token(models.Model):
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey('auth.User')
    token = models.CharField(max_length=32)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return "%s - %s" % (self.owner.username, self.token)