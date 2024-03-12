from django.urls import path
from rest_framework import routers
from lms.views.course import CourseViewSet
from lms.views.lesson import LessonListView, LessonDetailView, LessonCreateView, LessonUpdateView, LessonDeleteView

urlpatterns = [
    path('', LessonListView.as_view()),
    path('<int:pk>/', LessonDetailView.as_view()),
    path('create/', LessonCreateView.as_view()),
    path('update/<int:pk>/', LessonUpdateView.as_view()),
    path('delete/<int:pk>/', LessonDeleteView.as_view()),
]

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns += router.urls