from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TODO(models.Model):
    status_choices = [
    ('COMPLETED', 'COMPLETED'),
    ('PENDING', 'PENDING'),
    ]
    priority_choices = [
    (1,'1️'),
    (2, '2️'),
    (3, '3️'),
    (4, '4️'),
    (5, '5️'),
    (6, '6️'),
    (7, '7️'),
    (8, '8️'),
    (9, '9️'),
    (10, '10'),
    ]
    title = models.CharField(max_length=50)
    task = models.TextField(blank=False)
    status = models.CharField(max_length=20 , choices=status_choices)
    
    """ related name helps to connect priority with the user"""
    user  = models.ForeignKey(User  , on_delete= models.CASCADE, related_name='priority')
    date = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(max_length=2 , choices=priority_choices)

    def __str__(self):
        return self.title