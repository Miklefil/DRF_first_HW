from rest_framework import serializers, fields
from lms.models import Course, Subscription
from lms.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = fields.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'lesson_count', 'lessons', 'is_subscribed', 'price']
