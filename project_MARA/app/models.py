from django.db import models

# Create your models here.


class upload_file(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)