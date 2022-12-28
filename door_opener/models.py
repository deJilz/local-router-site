from django.db import models
from django.utils import timezone

# Create your models here.
class timeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class doorCycles(models.Model):
    # fields of the table
    time_of_POST_req = models.DateTimeField()
    prev_status_of_door = models.BooleanField
    csrf = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        ''' on save, update the timestamp'''
        if not self.id:
            self.time_of_POST_req = timezone.now()
        return super(doorCycles, self).save(*args, **kwargs)