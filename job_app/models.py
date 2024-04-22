

# Create your models here.
# models.py
from django.db import models

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / job_photos/<filename>
    return 'job_photos/{0}'.format(filename)

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, null=True)

    def __str__(self):
        return self.title
