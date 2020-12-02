from django.db import models
from django.utils import timezone
 

# Create your models here.

class Logger(models.Model):

    DEBUG = 'DG'
    INFO = 'IN'
    WARNING = 'WR'
    ERROR = 'ER'
    CRITICAL = 'CR'
    SEVERITY = [
        (CRITICAL, 'Critical'),
        (ERROR, 'Error'),
        (WARNING, 'Warning'),
        (INFO, 'Info'),
        (DEBUG, 'Debug'),
    ]
    

    message = models.CharField(max_length=256)
    date_time = models.DateTimeField(default=timezone.now)

    severity = models.CharField(
        max_length=2,
        choices=SEVERITY,
        default=INFO,
    )


    def __str__(self):
        return f'{self.severity} {self.date_time} {self.message}'
    
