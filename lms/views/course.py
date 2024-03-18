from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from lms.models import Course
from lms.paginations import CoursePagination
from lms.serializers.course import CourseSerializer
from users.permissions import IsModerator, IsOwner


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    pagination_class = CoursePagination

    def get_queryset(self):
        user = self.request.user
        if user.is_moderator:
            return Course.objects.all()
        return Course.objects.filter(owner=user)

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.user = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action in ['list', 'retrieve', 'update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]