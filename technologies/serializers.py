# backend/serializers.py
from rest_framework import serializers
from technologies.models import Technology


class TechnologySerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    def get_progress(self, obj):
        return obj.progress()

    class Meta:
        model = Technology
        fields = ['name', 'aim', 'image', 'progress']
