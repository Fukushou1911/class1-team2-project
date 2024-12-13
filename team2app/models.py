from django.db import models
from django.contrib.auth.models import User

class LostItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_lost = models.DateField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='lost_items/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
User.add_to_class('thank_you_points', models.PositiveIntegerField(default=0))
