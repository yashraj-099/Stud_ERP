# Task: Add Teacher, Course, and Department Tables to Admin Dashboard

## Current Work
Implementing tables for Teachers, Courses, and Departments in admin_dashboard.html similar to Student Table, including CRUD functionalities, scrolling sidebar links, and detail modals. This involves creating a new Department model and full CRUD setup for all three entities.

## Key Technical Concepts
- Django Models: Extending with Department model (name, description).
- Django Forms: ModelForms for Teacher, Course, Department (similar to StudentForm).
- Django Class-Based Views: ListView, DetailView, CreateView, UpdateView, DeleteView for each entity.
- Django URLs: Namespaced paths for CRUD operations.
- Django Templates: Extending student templates for lists, forms, details, deletes.
- HTML/JS: Table structures with Tailwind, modals for details, sidebar scrolling with anchor links.
- Django Admin: Register new model.
- Migrations: For new model.

## Relevant Files and Code
- models.py: Add Department model.
  - class Department(models.Model): name = models.CharField(...), description = models.TextField(...).
- forms.py: Add TeacherForm, CourseForm, DepartmentForm.
  - from django import forms; class TeacherForm(forms.ModelForm): class Meta: model = teacher, fields = ['name', 'email', 'phone', 'department', 'hire_date'].
  - Similar for others.
- views.py: Add CRUD views.
  - class TeacherListView(ListView): model = teacher, template_name = 'stud/teacher_list.html', context_object_name = 'teachers'.
  - Similar for DetailView, CreateView, UpdateView, DeleteView.
  - Update admin_dashboard: departments = Department.objects.all(); pass to context.
- urls.py: Add paths.
  - path('teachers/', TeacherListView.as_view(), name='teacher-list'), path('teachers/add/', TeacherCreateView.as_view(), name='teacher-add'), etc.
  - Similar for courses and departments.
- admin.py: from .models import Department; admin.site.register(Department).
- templates/stud/teacher_list.html: Update to proper list template (copy from student_list.html structure).
- Create: stud/course_list.html, stud/department_list.html, stud/teacher_form.html, stud/teacher_detail.html, stud/teacher_confirm_delete.html, etc. (copy and adapt from student equivalents).
- templates/dashboard/admin_dashboard.html: Add sections for Teacher Table (columns: Name, Email, Phone, Department, Hire Date, Actions), Course Table (Course Name, Code, Credits, Description, Actions), Department Table (Name, Description, Actions). Add ids like "teachers-table". Update sidebar links to href="#teachers-table" etc. Add modals for each (copy student modal, adapt fields).
- serializers.py: May need TeacherSerializer, CourseSerializer, DepartmentSerializer if API used, but focus on web CRUD.

## Problem Solving
- No existing CRUD for teachers/courses/departments: Creating full setup to match student functionality.
- No Department model: Adding simple model; teacher.department will be updated to FK later if needed.
- teacher_list.html has wrong content (login form?): Overwriting with proper list template.
- No course_list.html/department_list.html: Creating them.
- Sidebar scrolling: Update JS to handle multiple anchor links.
- Data: Tables will show existing data; empty if none.

## Pending Tasks and Next Steps
1. Add Department model to models.py.
   - "Create Department model in models.py with name and description fields."
2. Add Forms to forms.py (TeacherForm, CourseForm, DepartmentForm).
   - "Add ModelForms for Teacher, Course, Department in forms.py."
3. Add CRUD views to views.py for Teacher, Course, Department.
   - "Implement ListView, DetailView, CreateView, UpdateView, DeleteView for each in views.py."
4. Update admin_dashboard view in views.py to pass departments.
   - "In admin_dashboard, add departments = Department.objects.all() and pass to context."
5. Add CRUD URLs to urls.py for teachers, courses, departments.
   - "Add paths like path('teachers/add/', TeacherCreateView.as_view(), name='teacher-add'), etc., for all CRUD operations."
6. Register Department in admin.py.
   - "Add from .models import Department; admin.site.register(Department)."
7. Update/create templates in stud/:
   - "Update teacher_list.html to match student_list.html structure (list with add, actions)."
   - "Create course_list.html, department_list.html (copy from student_list.html, adapt fields)."
   - "Create teacher_form.html, teacher_detail.html, teacher_confirm_delete.html (copy from student equivalents, adapt fields)."
   - "Create same for course and department: course_form.html, etc."
8. Update admin_dashboard.html:
   - "Add Teacher Table section after Student Table: id='teachers-table', columns for teacher fields, Add button to teacher-add URL, Actions to detail/edit/delete, modal for details."
   - "Add Course Table: id='courses-table', columns for course fields, Add to course-add, etc."
   - "Add Department Table: id='departments-table', columns for name/description, Add to department-add, etc."
   - "Update sidebar links: Teachers to href='#teachers-table', Courses to '#courses-table', Departments to '#departments-table'."
   - "Update JS for sidebar to handle scrolling for all new anchors."
9. Run migrations.
   - "Execute: cd Stud_ERP/student && python manage.py makemigrations stud && python manage.py migrate."
10. Test implementation.
    - "Launch server if not running, login as admin, verify dashboard shows all tables with data (create sample via admin if empty), test sidebar scrolling to each table, test View modal, test Add/Edit/Delete flows for each entity (redirects work, forms save data)."
    - "Check for JS errors in console, ensure no broken links."

Progress will be tracked by updating this TODO.md after each step completion.
