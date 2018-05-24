from django.contrib.auth.models import User, Group
from django.db import models
from DepUpdate.models import course


class Notif(models.Model):

    title = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    related_course = models.ForeignKey(course,on_delete=models.CASCADE)
    uploaded_for = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

