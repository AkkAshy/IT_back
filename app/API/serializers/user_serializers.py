from rest_framework import serializers
from app.Users.models import UserProfile
from app.courses.models import Course

class UserSerializer(serializers.ModelSerializer):

    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())  # Добавляем курс

    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'phone', 'registered_at', 'contacted', 'course']