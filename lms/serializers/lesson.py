from rest_framework import serializers
from lms.models import Course, Lesson
from lms.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='video_link')]
