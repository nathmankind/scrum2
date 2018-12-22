from rest_framework import serializers
from .models import *


class ScrumGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrumGoal
        fields = ('visible', 'id', 'name', 'status')


class ScrumUserSerializer(serializers.ModelSerializer):
    scrumgoal_set = ScrumGoalSerializer(many=True)
    class Meta:
        model = ScrumUser
        fields = ('nickname', 'scrumgoal_set')