from django.contrib import admin

from .models import *

#admin.site.register(Notes)
#admin.site.register(Homeworks)
#admin.site.register(Todo)
admin.site.register(Student)


@admin.register(FichierPdf)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','fileType','course_file']
