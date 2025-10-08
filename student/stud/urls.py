from django.urls import path, include
from . import views
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, TeacherViewSet
from .views import (
    StudentListView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    StudentDetailView,
    student_login
)

router = DefaultRouter()
router.register(r'students' , StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'attendance', views.AttendanceViewSet)
router.register(r'results', views.ResultsViewSet)
router.register(r'parents', views.ParentViewSet)
router.register(r'classrooms', views.ClassroomViewSet)
router.register(r'notices', views.NoticeViewSet)    
app_name = 'stud'

urlpatterns = [
# --- API URLs ---
    path('api/', include(router.urls)),
    path('api/student/login/', student_login, name='student_login'),
# --- Web CRUD URLs ---
    path('', StudentListView.as_view(), name='student-list'),
    path('add/', StudentCreateView.as_view(), name='student-add'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student-edit'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]