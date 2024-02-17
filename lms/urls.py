from django.urls import path
from rest_framework import routers
from lms.views.course import CourseViewSet
from lms.views.lesson import LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('create/', LessonListCreateAPIView.as_view(), name='lesson_create'),
    path('<int:pk>/update/', LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson_retrieve_update_destroy'),
]

router = routers.SimpleRouter()
router.register(r'course', CourseViewSet)

urlpatterns += router.urls