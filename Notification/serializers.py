from rest_framework import serializers
from .models import Notif

class NotifSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notif
        fields = ['title' , 'uploaded_by', 'related_course']

