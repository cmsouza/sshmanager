from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Host(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('auth.User')
    category = models.ForeignKey('Category')
    host = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    port = models.IntegerField(default=22)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def has_owner(self):
        return self.owner_id is not None

    def full_host(self):
        return self.category.name_chain() + '.' + self.host

    def __str__(self):
        return "%s@%s:%d" % (self.user, self.hostname, self.port)

class Token(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('auth.User')
    token = models.CharField(max_length=32)
    obs = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def has_owner(self):
        return self.owner_id is not None

    def __str__(self):
        return str(self.token)

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    parent = models.ForeignKey('self', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args, kwargs)

    def has_owner(self):
        return self.owner_id is not None

    def name_chain(self):
        chain = [self.slug]

        if self.parent is not None:
            chain.insert(0, self.parent.name_chain())

        return ".".join(chain)

    def __str__(self):
        return self.name_chain()