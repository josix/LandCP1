from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class set_number(models.Model):

    number=models.IntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __unicode__(self):

            return self.number,self.created_date


class set_time(models.Model):

    start=models.DateTimeField(default=timezone.now)
    end=models.DateTimeField(blank=True, null=True)

    def __unicode__(self):

            return self.start,self.end 


class attendence(models.Model):
    attend=models.NullBooleanField()
    student = models.CharField(max_length = 9)
    date = models.DateTimeField(default = timezone.now)
