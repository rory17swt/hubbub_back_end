from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

# Create your models here.
class Event(models.Model):
    owner = models.ForeignKey(
        to='users.User',
        related_name='events',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    duration = models.DurationField()
    contact_email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True, storage=MediaCloudinaryStorage)

    def __str__(self):
        return self.title
    
