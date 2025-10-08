from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import StudentForm  
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Student, course, teacher, attendance, results, notice, parent, classroom
from .serializers import StudentSerializer, CourseSerializer, TeacherSerializer, AttendanceSerializer, ResultsSerializer, NoticeSerializer, ParentSerializer, ClassroomSerializer


# course ViewSet
class CourseViewSet(viewsets.ModelViewSet):
    queryset = course.objects.all()
    serializer_class = CourseSerializer

# teacher ViewSet
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = teacher.objects.all()
    serializer_class = TeacherSerializer

# attendance ViewSet
class AttendanceViewSet(viewsets.ModelViewSet): 
    queryset = attendance.objects.all()
    serializer_class = AttendanceSerializer
# results ViewSet
class ResultsViewSet(viewsets.ModelViewSet):    
    queryset = results.objects.all()
    serializer_class = ResultsSerializer


# Notice ViewSet        
class NoticeViewSet(viewsets.ModelViewSet):
    queryset = notice.objects.all()
    serializer_class = NoticeSerializer
# Parent ViewSet
class ParentViewSet(viewsets.ModelViewSet):
    queryset = parent.objects.all()
    serializer_class = ParentSerializer
# Classroom ViewSet
class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = classroom.objects.all()
    serializer_class = ClassroomSerializer

# XYZ ViewSet


# --- REST API PART ---
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# --- REGULAR CRUD VIEWS ---

def home(request):
    students = Student.objects.all()
    today = date.today()  # get current date
    return render(request, 'stud/student_list.html', {'students': students, 'today': today})


class StudentListView(ListView):
    model = Student
    template_name = 'stud/student_list.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        return context  

class StudentDetailView(DetailView):
    model = Student
    template_name = 'stud/student_detail.html'
    

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'stud/student_form.html'
    success_url = reverse_lazy('stud:student-list')  # <- namespace included

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'stud/student_form.html'
    success_url = reverse_lazy('stud:student-list')  # <- namespace included

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'stud/student_confirm_delete.html'
    success_url = reverse_lazy('stud:student-list')  # <- namespace included






#Student Login View
@api_view(['POST'])
def student_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        student = Student.objects.get(email=email, password=password)
        return Response({
            'message': 'Login successful',
            'student': {
                'id': student.id,
                'name': student.name,
                'email': student.email,
                'age': student.age,
                'course': student.course
            }
        })

    except Student.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    