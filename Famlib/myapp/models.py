from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import uuid

    
class Library(models.Model):
    name = models.CharField(max_length=20)
    library_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()

    class Meta:
        app_label = 'myapp'

 # user table
class Users(models.Model):
    username = models.CharField( primary_key=True, max_length=100, unique=True)
    libraryid = models.UUIDField()
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    password = models.CharField(max_length=20)
    married = models.BooleanField(default=False)
    userlevel=models.IntegerField(default=1)
    class Meta:
        app_label = 'myapp'

def validate_file_size(value):
    filesize = value.size
    if filesize > 10 * 1024 * 1024:
        raise ValidationError(_("The maximum file size that can be uploaded is 10MB"))

# Create your models here.
class Message(models.Model):
    mid=models.AutoField(primary_key=True,default=1,editable=False)
    type=models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    heading = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.username,self.message
import datetime
class Book(models.Model):
    id=models.CharField( primary_key=True, max_length=100,unique=True,editable=False)
    title=models.CharField(max_length=50)
    tags=models.CharField(max_length=100)
    desc=models.CharField(max_length=300)
    date=models.DateField(default=datetime.date.today)
    blevel=models.IntegerField(default=3)
    file=models.FileField(upload_to='upload/',validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc','docs','txt','zip','.py','jpg','jpeg','png','docx', 'xls', 'xlsx', 'ppt'
                                                                                                      ,'pptx']),validate_file_size])
    username = models.CharField(max_length=40,default='asjad')
    class Meta:
        app_label = 'myapp'

    def __str__(self):
        return self.title

