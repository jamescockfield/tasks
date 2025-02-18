from rest_framework import serializers
from django.contrib.auth.models import User
from tasks.models.models import UserProfile, Project, TaskList, Task

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'notification_preferences']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='userprofile')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']
        read_only_fields = ['id']

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        user = super().create(validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', None)
        user = super().update(instance, validated_data)
        
        if profile_data:
            UserProfile.objects.update_or_create(
                user=user,
                defaults=profile_data
            )
        return user