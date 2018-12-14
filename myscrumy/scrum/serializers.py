from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ScrumGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrumGoal
        fields = ('visible', 'id', 'name', 'status')


class ScrumUserSerializer(serializers.ModelSerializer):
    scrumgoal_set = ScrumGoalSerializer(many=True)
    class Meta:
        model = ScrumUser
        fields = ('nickname', 'scrumgoal_set')