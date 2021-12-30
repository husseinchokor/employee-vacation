from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save

class Employee(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=CASCADE)

class Vacation(models.Model):
    employee = models.ForeignKey(Employee, blank=False, null=False, on_delete=CASCADE)
    description = models.TextField(blank=False, null=False)
    from_date = models.DateField(blank=False, null=False)
    to_date = models.DateField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)

'''
Auto create employee when create a User
'''
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     Employee.objects.create(id=instance.id, user=instance)
