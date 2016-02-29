from rest_framework import serializers
from pages.models import Register, Event

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('id', 'timestamp')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'nfc_tag_id', 'timestamp', 'message')
