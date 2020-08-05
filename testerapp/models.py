from django.db import models

# Create your models here.
class BugInfo(models.Model):
    bugId = models.CharField(max_length=16,primary_key=True)
    bugDesc = models.CharField(max_length=72)
    currBuild = models.CharField(max_length=11)
    dateRaised = models.DateField()
    appName = models.CharField(max_length=11)
    detectedBy = models.CharField(max_length=30)
    bugStatus = models.CharField(max_length=9)
    fixedBy = models.CharField(max_length=30)
    bugPriority = models.CharField(max_length=7)