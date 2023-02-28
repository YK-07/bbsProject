from django.db import models
from django.contrib.auth.models import User

# Create your models here.

EVALUATION_CHOICES = [('良い', '良い'),('悪い', '悪い')]
class bbsModel(models.Model):
    university = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    content = models.TextField()
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='',null=True, blank=True)
    useful_review = models.IntegerField(null=True, blank=True, default=0)
    useful_review_recode = models.TextField(null=True, blank=True)
    evaluation = models.CharField(max_length=10, choices=EVALUATION_CHOICES,null=True, blank=True)