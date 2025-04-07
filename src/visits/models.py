from django.db import models


# Create your models here.
class PageVisits(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    path = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
