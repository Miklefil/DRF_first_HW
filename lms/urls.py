from django.urls import path
from rest_framework import routers
from lms.views.course import CourseViewSet
from lms.views.lesson import LessonListView, LessonDetailView, LessonCreateView, LessonUpdateView, LessonDeleteView
from lms.views.subscription import SubscribeAPIView

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    path('<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('create/', LessonCreateView.as_view(), name='lesson_create'),
    path('update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),
    path('delete/<int:pk>/', LessonDeleteView.as_view(), name='lesson_delete'),
    path('subscription/', SubscribeAPIView.as_view(), name='subscription'),
]

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns += router.urls