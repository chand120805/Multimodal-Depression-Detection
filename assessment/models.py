from django.db import models
from django.contrib.auth.models import User

class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # PHQ scores (0–3)
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()

    # Detailed answers (text)
    text1 = models.TextField(blank=True, null=True)
    text2 = models.TextField(blank=True, null=True)
    text3 = models.TextField(blank=True, null=True)
    text4 = models.TextField(blank=True, null=True)
    text5 = models.TextField(blank=True, null=True)
    text6 = models.TextField(blank=True, null=True)
    text7 = models.TextField(blank=True, null=True)
    text8 = models.TextField(blank=True, null=True)

    total_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)