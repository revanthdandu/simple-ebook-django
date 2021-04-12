from django.db import models


class Books(models.Model):
    image = models.ImageField(upload_to='bookspics')
    name = models.CharField(max_length=200)
    description = models.TextField()
    bookpdf = models.FileField(upload_to='bookpdf')

