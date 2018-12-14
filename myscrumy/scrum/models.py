from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ScrumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname

    class Meta:
        ordering = ['nickname']


class ScrumGoal(models.Model):
    visible = models.BooleanField(default=True)
    user = models.ForeignKey(ScrumUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    status = models.IntegerField(default=-1)

    '''
    0 = Weekly Goal
    1 = Daily Goal
    2 = Verify
    3 = Done
    '''

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-id']
