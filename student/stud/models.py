from django.db import models
# Create your models here.
# Student Model
class Student(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly defining primary key
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, default='')
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=100, default='')
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.name

   
# Course Model  
class course(models.Model):
    course_name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    credits = models.IntegerField()

    def __str__(self):
        return self.course_name

#class_room Model
class classroom(models.Model):
    name = models.CharField(max_length=50)                      # e.g. "Class 10A"
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='classrooms')
    teacher = models.ForeignKey('teacher', on_delete=models.CASCADE, related_name='classrooms')
    students = models.ManyToManyField(Student, related_name='classrooms')

    def __str__(self):
        return self.name

# parent Model
class parent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    passward = models.CharField(max_length=128, default='')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    students = models.ManyToManyField(Student, related_name='parents')
    
    def __str__(self):
        return self.name

# teacher Model
class teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, default='')
    phone = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return self.name


# attendance Model
class attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10)  # Present, Absent, etc.
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"

#Notice Model
class notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    created_by = models.ForeignKey(teacher, on_delete=models.CASCADE, related_name='notices')
    def __str__(self):
        return self.title 

# results Model
class results(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='result_records')
    subject = models.CharField(max_length=100)
    marks = models.FloatField()
    grade = models.CharField(max_length=2, blank=True)  # e.g., A+, B, C
    exam_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        # Automatically calculate grade based on marks
        if self.marks >= 90:
            self.grade = 'A'
        elif self.marks >= 80:
            self.grade = 'B'
        elif self.marks >= 70:
            self.grade = 'C'
        elif self.marks >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.subject} - {self.grade}"



#<--We can also add more models like Exams,
# Subjects, Timetable, Fees, Library, 
# Transportation, Events, etc. as per requirements.--> 