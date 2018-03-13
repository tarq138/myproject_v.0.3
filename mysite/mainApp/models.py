from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return "%s) Пользователь  %s" % (self.id, self.name)

    class Meta:
        verbose_name = 'Mysubscriber'
        verbose_name_plural = 'A lot of Subscribers'