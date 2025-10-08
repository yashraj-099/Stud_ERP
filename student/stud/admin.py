from django.contrib import admin

# Register your models here.
from .models import Student, course, teacher, attendance, results, classroom, parent, notice # Import the models
admin.site.register(Student)
admin.site.register(teacher)
admin.site.register(attendance)
admin.site.register(results)
admin.site.register(course)
admin.site.register(classroom)
admin.site.register(parent)
admin.site.register(notice)
admin.site.site_header = "Student Management Admin"
admin.site.site_title = "Student Management Admin Portal"
admin.site.index_title = "Welcome to Student Management Portal"


# Admin Name -- hp
# Admin Password -- admin123