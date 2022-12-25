from django.db import models

# Create your models here.
class Career(models.Model):
    career = models.CharField(max_length=100)
    def __str__(self):
        return self.career

GENDER = (
    ('F','F'),
    ('M','M'),
)

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)