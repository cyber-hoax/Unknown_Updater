from django.db import models

# Create your models here.

class UserDetail(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hybrid_uid = models.CharField(max_length=50, default="")
    
    