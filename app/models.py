from django.db import models
from django.contrib.auth.models import User

COURSES = (
    ('PH','Langage php'),
    ('EN','English langage'),
    ('MA','Databases'),
    ('PY','Langage python'),
    ('JV','Java'),
    ('HCS','HTML and CSS'),
    ('XM','XML'),
    ('C','Langage C'),
    ('DJ','DJANGO'),
)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile=models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name

class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
            return self.title
                
    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"

class Homeworks(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=50)
    due = models.DateTimeField()
    is_finished = models.BooleanField(default = False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "homeworks"
        verbose_name_plural = "homeworks"

        
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    is_finished = models.BooleanField(default = False)

    def __str__(self):
        return self.title
        
class FichierPdf(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    fileType = models.CharField(choices=COURSES, max_length=50)
    course_file = models.FileField(upload_to='cours')