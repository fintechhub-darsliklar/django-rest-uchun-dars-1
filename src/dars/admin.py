from django.contrib import admin
from .models import Universitet, Teacher, Student, Group
# Register your models here.

admin.site.register(Universitet)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
