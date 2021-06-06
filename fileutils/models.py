import hashlib, os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone

from rest_framework import serializers

fs = FileSystemStorage()
class Upload(models.Model):
    filename = models.TextField(null=True)
    filesize = models.IntegerField(null=True)
    fileext = models.TextField(null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    dtm = models.DateTimeField(default=timezone.now) 
    file = models.FileField(storage=fs,null=True)
    digest = models.TextField(null=True)
    score = models.IntegerField(null=True)
    def save(self, *args, **kwargs):
        self.filename = self.file.name
        self.filesize = self.file.size
        self.fileext = os.path.splitext(self.file.name)[1]
        if(self.fileext  !='.txt'):
            raise serializers.ValidationError({'message':'Invalid file type. File must be of type .txt'}, code=415)
        self.digest = self._calc_digest(self.file)
        super().save(*args, **kwargs)

    def _calc_digest(self,f):
        hash = hashlib.sha1()
        if f.multiple_chunks():
            for chunk in f.chunks():
                hash.update(chunk)
        else:
            blob=f.read()
            hash.update(blob)
        h = hash.hexdigest()
        return h
        
    def update_score(self,score):
        self.score = self.score
        super().save(*args, **kwargs)
