from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from lms.models import Lesson
from lms.paginations import LessonPagination
from lms.serializers.lesson import LessonSerializer
from users.permissions import IsModerator, IsOwner


class LessonCreateView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()


class LessonUpdateView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()


class LessonDetailView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDeleteView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LessonListView(ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = LessonPagination

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='moderator').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(course__user=user)
