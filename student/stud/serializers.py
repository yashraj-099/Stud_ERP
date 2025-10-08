from rest_framework import serializers
from .models import Student, course, teacher, attendance, results, parent, classroom, notice    

# serializer for Student model
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# serializer for course model
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = '__all__'

# serializer for teacher model
class TeacherSerializer(serializers.ModelSerializer):   
    class Meta:
        model = teacher
        fields = '__all__'

# serializer for parent model
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = parent
        fields = '__all__'

# serializer for attendance model
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendance
        fields = '__all__'

# serializer for results model
class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = results
        fields = '__all__'
        #you can also specify fields like ['student', 'subject', 'marks', 'grade', 'exam_date'] 
        #or exclude = ['created_at', 'updated_at']
        
# serializer for notice model
class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = notice
        fields = '__all__'

# serializer for classroom model
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = classroom
        fields = '__all__'




