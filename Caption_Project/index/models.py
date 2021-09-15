from django.db import models
from django.utils import timezone
import os
from uuid import uuid4
from django.contrib.auth.models import User
# User._meta.get_field('email')._unique = True



def path_and_rename(instance, filename):        #used for renaming image
    upload_to = ''
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
    

class Image(models.Model):
    image=models.FileField(upload_to=path_and_rename,max_length=255)


class Caption(models.Model):
    imageURL = models.FileField(upload_to=path_and_rename, max_length=255, null=True)
    caption1=models.TextField()
    caption2=models.TextField()
    caption3=models.TextField()
    caption4=models.TextField()
    caption5=models.TextField()
    
   

#     # def __str__(self):
#     #     return self.title
