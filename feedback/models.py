from django.db import models

class Feedback(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()
    class Meta:
        db_table = "Feedbacks"

# Create your models here.
