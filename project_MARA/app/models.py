from django.db import models
import os
from uuid import uuid4




class upload_file(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)