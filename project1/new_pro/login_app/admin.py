from django.contrib import admin

# Register your models here.

from .models import SuperSchool
from .models import Course,Clossroom,Teacher,Student


admin.site.register(SuperSchool)
admin.site.register(Clossroom)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)



