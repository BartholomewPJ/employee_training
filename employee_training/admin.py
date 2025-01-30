from django.contrib import admin

# Register your models here.
from .models import Division
from .models import Employee
from .models import PersonalInfo
from .models import LearningCourse

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'division', 'get_courses')
    
    def get_courses(self, obj):
        return ", ".join([course.title for course in obj.learningcourse_set.all()])
    
    get_courses.short_description = 'Enrolled Courses'

admin.site.register(Division)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(PersonalInfo)
admin.site.register(LearningCourse)
