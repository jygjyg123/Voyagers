from django.db import models

# Create your models here.
class Survey(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    option1_count = models.IntegerField(null=True, blank=True)
    option2_count = models.IntegerField(null=True, blank=True)
    option3_count = models.IntegerField(null=True, blank=True)
    option4_count = models.IntegerField(null=True, blank=True)