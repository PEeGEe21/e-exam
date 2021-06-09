from django.contrib import admin
from .models import Student, Teacher, Paper, Exam, Grade


# admin.site.register(Exam)
admin.site.site_header = 'CCU Online examination system'
admin.site.site_title = 'Online Exam System'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # What information to display
    list_display = ('id', 'name', 'sex', 'dept', 'major', 'email')
    # What information can you click to enter the edit page
    list_display_links = ('id', 'name')
    # Specify the field to search, a search box will appear for the administrator to search for keywords
    search_fields = ['name', 'dept', 'major']
    # Specify a list filter, a quick filter option will appear on the right
    List_filter = ['name', 'dept', 'major']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'sex', 'dept', 'email')
    list_display_links = ('id', 'name', 'username')
    search_fields = ['name', 'dept', 'username']
    list_filter = ['name', 'dept', 'username']


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'question', 'option1', 'option2', 'option3', 'option4', 'answer', 'score')


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'tid', 'course', 'instruction', 'major', 'exam_time')
    # Specify the field to search, a search box will appear for the administrator to search for keywords
    search_fields = ['course', 'major', 'exam_time']
    # Specify a list filter, a quick filter option will appear on the right
    List_filter = ['course', 'major', 'exam_time']


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'sid', 'subject', 'grade')






